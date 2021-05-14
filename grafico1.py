import plotly.express as px
import numpy as np
import pandas as pd

data_df = pd.read_csv('https://raw.githubusercontent.com/josueramalho/visualizacao-da-informacao/master/file.csv')
index = pd.Series(data_df['causa'])

y_data = data_df['causa']
x_data= data_df['total_global']
fig = px.bar(index, x_data, y_data, orientation='h')
fig.show()