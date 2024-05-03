import streamlit as st
import plotly.express as px
import pandas as pd
st.title('Análise Spotify')

st.subheader('Como a popularidade média das músicas mudou de 2000 a 2019?')

df = pd.read_csv('songs_normalize.csv')

pop_media = df.groupby('year')['popularity'].mean().reset_index()

fig = px.line(pop_media, x='year', y='popularity', markers=True)
st.plotly_chart(fig, use_container_width=True)

st.write('Não foi observado uma mudança drástica da média durante os anos. Apenas nos extremos, que não deveriam estar na base, e em 2018, que superou a marca de 70.')

st.subheader('Quais são os 5 gêneros mais comuns entre as principais faixas?')

df_novo = df.copy()
df_novo['genre'] = df_novo['genre'].str.replace(' ', '').str.split(',')
df_novo = df_novo.explode('genre')

top_genres = df_novo['genre'].value_counts().head(5)

fig_genres = px.bar(top_genres)
st.plotly_chart(fig_genres, use_container_width=True)

st.write('Explicação do gráficos - o mais comum é pop')

st.subheader('Qual é a distribuição das durações das músicas entre as principais faixas do Spotify?')

df['duration_min'] = df['duration_ms']/60000
fig_duration = px.histogram(df, x='duration_min', nbins=50)
fig_duration.update_traces(marker_line_color='black', marker_line_width=1.5)
st.plotly_chart(fig_duration, use_container_width=True)

st.write('A maior concentração está em torno de 3 minutos e meio')

