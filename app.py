"""Aplicação Flask que prevê ocupação com base em sensores e armazena os dados no MongoDB."""

import pickle
import pandas as pd

from flask import Flask, request, render_template
from pymongo import MongoClient
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

client = MongoClient(
    "mongodb+srv://admin:85200285.luS@clusternovo.fle4g.mongodb.net/"
    "?retryWrites=true&w=majority&appName=Clusternovo"
)
db = client["detecocup"]
collection = db["ocupacao2"]

with open('models/arvore_from_pickle.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route("/")
def index():
    """Rota principal que exibe o formulário inicial."""
    return render_template("index.html")


@app.route("/form", methods=['GET', 'POST'])
def form():
    """Recebe os dados do formulário, faz a previsão e salva no banco."""
    if request.method == 'POST':
        temperatura = float(request.form.get("temperatura"))
        umidade = float(request.form.get("umidade"))
        luz = float(request.form.get("luz"))
        co2 = float(request.form.get("co2"))
        humidade_relativa = float(request.form.get("humidade_relativa"))

        entrada_df = pd.DataFrame([{
            'Temperature': temperatura,
            'Humidity': umidade,
            'Light': luz,
            'CO2': co2,
            'HumidityRatio': humidade_relativa
        }])

        predicao = model.predict(entrada_df)[0]
        resultado = "Local Ocupado" if predicao == 1 else "Local Vazio"

        registro = entrada_df.copy()
        registro['Predicao'] = resultado
        collection.insert_one(registro.to_dict(orient='records')[0])

        dados = pd.DataFrame({
            'Variável': ['Temperatura', 'Umidade', 'Luz', 'CO2', 'Umidade Relativa'],
            'Valor': [temperatura, umidade, luz, co2, humidade_relativa]
        })
        figura = px.bar(dados, x='Variável', y='Valor', title='Valores informados')
        grafico = pio.to_html(figura, full_html=False)

        return render_template("form.html", predicao=resultado, grafico=grafico)

    return render_template("form.html")


@app.route("/graficos")
def graficos():
    """Gera gráficos baseados nos registros do banco de dados."""
    registros = list(collection.find())
    if not registros:
        return render_template("graficos.html", graficos=[])

    df = pd.DataFrame(registros)

    colunas = ['Temperature', 'Humidity', 'Light', 'CO2', 'HumidityRatio']
    for col in colunas:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    graficos_gerados = []

    freq = df['Predicao'].value_counts().reset_index()
    freq.columns = ['Estado', 'Frequência']
    fig1 = px.bar(freq, x='Estado', y='Frequência', title='Frequência de Ocupação')
    graficos_gerados.append(pio.to_html(fig1, full_html=False))

    for var in colunas:
        fig = px.box(df, x='Predicao', y=var, title=f'{var} por Ocupação')
        graficos_gerados.append(pio.to_html(fig, full_html=False))

    importancias = model.feature_importances_
    nomes_variaveis = ['Temperature', 'Humidity', 'Light', 'CO2', 'HumidityRatio']
    df_importancias = pd.DataFrame({
        'Variável': nomes_variaveis,
        'Importância': importancias
    }).sort_values(by='Importância', ascending=False)

    fig_importancia = px.bar(df_importancias, x='Variável', y='Importância',
                             title='Importância de Cada Variável no Modelo')
    graficos_gerados.append(pio.to_html(fig_importancia, full_html=False))

    return render_template("graficos.html", graficos=graficos_gerados)


if __name__ == "__main__":
    app.run(debug=True)
