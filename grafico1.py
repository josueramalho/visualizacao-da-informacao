import plotly.express as px
import pandas as pd

# Importando arquivo CSV que será usado
dataset = pd.read_csv('https://github.com/josueramalho/visualizacao-da-informacao/raw/master/src/dataset.csv')
dataset = pd.DataFrame(dataset)
# Selecionando e tratando apenas os dados que serão usados no gráfico 1
deaths_df = dataset.loc[dataset['Year'] == 2017]
world_deaths = deaths_df.loc[deaths_df['Entity'] == 'World']
world_deaths = world_deaths.drop(['Entity', 'Code', 'Year'], axis=1)
world_deaths = world_deaths.sort_values(by = 6573, axis=1, ascending=False)
# Criando novo dataset com dados tratados
x_data = list(world_deaths.loc[6573])
y_data = list(world_deaths.columns)
# Criando gráfico
fig = px.bar(x=x_data, y=y_data, orientation='h', labels={'y': 'Causa', 'x': 'Mortes (em milhões)', 'text':'Float'},
            title='Principais causas de morte no mundo em 2017 (Fonte: OMS)', text=x_data, range_y=[0, 10])
# Renderizando gráfico
fig.show()