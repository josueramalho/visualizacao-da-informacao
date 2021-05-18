import pandas as pd
from plotly import graph_objects as go
# Importando dataset base
file_url = 'https://github.com/josueramalho/visualizacao-da-informacao/raw/master/src/dataset.csv'
dataset = pd.read_csv(file_url)
dataset = pd.DataFrame(dataset)
# Tratando dataset e selecionando os dados que serão usados
topic = 'Deaths - Road injuries - Sex: Both - Age: All Ages (Number)'
deaths_df = dataset.loc[dataset['Year'] == 2017, ['Entity','Year', topic]]
numbers = list(pd.Series(deaths_df[topic]))
entities = list(pd.Series(deaths_df.Entity))
# Removendo a entidade Mundo da lista
entities.pop(-4)
numbers.pop(-4)
# Criando imagem
fig = go.Figure(data=go.Choropleth(
    locations=entities,
    z = numbers,
    locationmode = 'country names',
    colorscale = ('yellow','orange','red'),
    colorbar_title = "Mortes",
    )
)
fig.update_layout(title_text='Mortes em acidentes de transito no mundo em 2017, segundo OMS ((Organização Mundial da Saúde)')
# Renderizando
fig.show()