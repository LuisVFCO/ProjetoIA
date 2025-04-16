from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

'''Carga do modelo preditivo'''
model = pickle.load(open('models/modelo_preditivo.pkl','rb'))

@app.route("/", methods=['GET','POST'])
def index():
    
    if request.method == 'POST':
        idade = int(request.form.get("idade"))
        sexo = int(request.form.get("sexo"))
        pressao = int(request.form.get("pressao"))
        potassio = float(request.form.get("potassio"))
        colesterol = int(request.form.get("colesterol"))
        
        respostas = [2,5,1,4,1]
        dados = pd.DataFrame({'Remedio':['Y','X','A','B','C'],
                              'Valor': respostas})
        
        figura = px.bar(dados, x='Remedio', y='Valor')
        grafico = pio.to_html(figura, full_html=False)

        caracteristicas = np.array([[idade, sexo, pressao, colesterol, potassio]])
        predicao = model.predict(caracteristicas)
        mapeamento = {0: 'Y', 1:'X', 2:'A', 3:'B', 4:'C'}
        resultado = mapeamento.get(predicao[0])
        return render_template('index.html', predicao = resultado, grafico=grafico)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
