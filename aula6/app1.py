# para executar:
# windows: python -m streamlit run <filename.py>
# outros: streamlit run <filename.py>
# talvez executar com sudo! + path inteiro no arquivo

import streamlit as st

st.title('Olá, mundo!')

st.header('Esse é um subtítulo! _algo em itálico_ **negrito**', divider='rainbow')

st.subheader('Subsubtítulo! :blue[bem legal, texto azul] :sunglasses:')

st.markdown('Esse é um markdown :tulip:. **Negrito**')

st.caption('Legenda para algum trecho, imagem, algo do tipo')

st.write('Texto comum')

st.divider()

codigo = '''def hello():
    print("Olá, mundo!")'''
st.code(codigo, language='python')

import pandas as pd
df = pd.DataFrame({'nomes':['Poliana', 'Ana', 'Alberto'], 'idades':[25, 40, 56]})
st.dataframe(df)

import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

df = pd.DataFrame(
    [[-23.5489, -46.6388], [-23.5489, -47.6388]],
    columns=['lat', 'lon'])

st.map(df)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.scatter_chart(chart_data)

df = pd.DataFrame({'Category': ['a', 'b', 'c', 'd'], 'Values':[23, 46, 56, 78]})

st.bar_chart(df, x='Category', y='Values')

import seaborn as sns
import matplotlib.pyplot as plt

plot = sns.barplot(data=df, x='Category', y='Values')
st.pyplot(plot.get_figure())

import plotly.express as px
fig = px.bar(df, x='Category', y='Values')
st.plotly_chart(fig, use_container_width=True)

# Voltamos 20:37


