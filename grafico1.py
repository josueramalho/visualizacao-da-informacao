import plotly.express as px
import pandas as pd

# Importando arquivo CSV que será usado
dataset = pd.read_csv('https://raw.githubusercontent.com/josueramalho/visualizacao-da-informacao/master/dataset_1.csv')
index = pd.Series(dataset['causa'])

# Separando dados para melhor visualização e tratamento
y_data = dataset['causa']
x_data= dataset['total_global']

# Criando o gráfico
fig = px.bar(index, x_data, y_data, orientation='h', labels={'y': 'Causa', 'x': 'Mortes (em milhões)'},
            title='10 Principais causas de morte no mundo em 2017 (Fonte: OMS)', text=x_data)
            
#Exibindo o gráfico
fig.show()