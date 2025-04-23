# 🛰️ Sistema de Detecção de Ocupação com Aprendizado de Máquina

Este projeto tem como objetivo detectar se um ambiente está ocupado ou vazio com base em dados captados por sensores ambientais. O sistema utiliza **machine learning** para realizar predições, armazenar os resultados em um banco de dados **MongoDB**, e exibir estatísticas visuais interativas em gráficos.

---

## 🧠 Como Funciona?

Ao inserir os valores de sensores como **temperatura**, **umidade**, **luminosidade**, **CO₂** e **razão de umidade**, o sistema utiliza um modelo preditivo treinado (`DecisionTreeClassifier`) para classificar o ambiente como:

- 🟩 **Local Ocupado**
- ⬜ **Local Vazio**

Os dados e as predições são salvos automaticamente em um banco de dados MongoDB e podem ser analisados por meio de gráficos interativos na aba "Ver Gráficos".

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Visual Studio Code (VSCode)** – ambiente de desenvolvimento
- **Flask** – framework web
- **scikit-learn** – modelo preditivo com árvore de decisão
- **pandas** e **numpy** – manipulação de dados
- **Plotly** – geração de gráficos interativos
- **MongoDB Atlas** – armazenamento em nuvem dos dados
- **pymongo** – conexão entre Flask e MongoDB
- **gunicorn** – servidor de produção (opcional para deploy)

---

## 📦 Requisitos

Antes de executar o projeto, instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## 🚀 Como Rodar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Instale os pacotes:
```bash
pip install -r requirements.txt
```

3. Execute o app:
```bash
python app.py
```

4. Acesse no navegador:
```
http://localhost:5000
```

---

## 👥 Equipe

Este projeto foi desenvolvido por:

- **Luis Vinicius Silva**
- **Alan Vitor Vitorino**
- **Adonis Vinicius Guedes**
- **João Victor Assis**

---

## 📌 Observações

- Os dados são inseridos manualmente via formulário na interface.
- O modelo de aprendizado foi treinado previamente com dados artificiais de sensores.
- O MongoDB armazena cada nova entrada e predição automaticamente.
- Projeto desenvolvido e executado no **Visual Studio Code**.

---

## 📊 Exemplos de Aplicação

- Monitoramento de salas de aula ou laboratórios
- Ambientes de coworking ou salas de reunião
- Controle de energia em ambientes automatizados
