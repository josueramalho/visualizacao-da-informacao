import pandas as pd
from matplotlib import pyplot as plt

#Importando dataset base
file_url = 'https://github.com/josueramalho/visualizacao-da-informacao/raw/master/src/dataset.csv'
dataset = pd.read_csv(file_url)
dataset = pd.DataFrame(dataset)
#Tratando dataset e selecionando os dados que serão usados
topic = 'Deaths - Road injuries - Sex: Both - Age: All Ages (Number)'
deaths_df = dataset.loc[dataset['Entity'] == 'World', ['Entity','Year', topic]]
numbers = list(pd.Series(deaths_df[topic]))
years = list(pd.Series(deaths_df.Year))
#Criando uma list para tornar mais simples e visualmente amigável o plot
deaths_df = [years, numbers]
# Criando o gráfico
plt.plot(years, numbers)
plt.title('Mortes no trânsito de 1990 a 2017, segundo a OMS (Organização Mundial da Saúde)')
plt.ylabel('Mortes (em milhões)')
# Renderizando
plt.show()