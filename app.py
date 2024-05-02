import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# Título do app
st.title('Análise Spotify')
df = pd.read_csv('songs_normalize.csv')
df.head()
st.divider()
st.subheader('Como a popularidade média das músicas mudou entre 2000 e 2019?')
pop_media = df.groupby('year')['popularity'].mean().reset_index()
fig = px.line(pop_media, x='year', y='popularity', markers=True, title='Média da Popularidade das músicas em cada ano',
              labels={'year': 'Ano', 'popularity': 'Popularidade Média'})
fig.update_layout(xaxis_title='Ano', yaxis_title='Popularidade Média', showlegend=False)

st.plotly_chart(fig, use_container_width=True)

st.write('Observa-se uma variação na popularidade média das músicas ao longo dos anos. Este gráfico nos ajuda a entender como as tendências musicais e a recepção do público evoluíram ao longo do tempo. A popularidade pode ser influenciada por diversos fatores como mudanças na indústria musical, plataformas de streaming e alterações no comportamento dos ouvintes.')
st.divider()
st.subheader('Quais são os 10 gêneros mais comuns entre as principais faixas do Spotify?')

# Calculate the top 10 most common genres
df_novo = df.copy()

df_novo['genre'] = df_novo['genre'].str.replace(' ', '').str.split(',')
df_novo = df_novo.explode('genre')


top_genres = df_novo['genre'].value_counts().head(10).reset_index().sort_values(by='count')
top_genres.columns = ['genre', 'count']
top_genres = top_genres.sort_values(by='count', ascending=False)

# Create a Plotly bar chart for the top 10 genres
fig_genres = px.bar(top_genres, x='count', y='genre', orientation='h', title='10 gêneros mais comuns entre as principais faixas do Spotify',
                    labels={'count': 'Quantidade', 'genre': 'Gênero'},
                    color='genre')

st.plotly_chart(fig_genres, use_container_width=True)

st.write('Este gráfico revela os gêneros mais frequentes nas listas de faixas populares do Spotify, destacando as preferências musicais predominantes entre os ouvintes. A análise dos gêneros mais populares pode indicar tendências de mercado e preferências culturais específicas.')
st.divider()
st.subheader('Qual é a distribuição das durações das músicas entre as principais faixas do Spotify?')

# Calculate the duration in minutes
df['duration_min'] = df['duration_ms'] / 60000

# Create a Plotly histogram for the distribution of song durations
fig_duration = px.histogram(df, x='duration_min', nbins=50, title='Distribuição das durações das músicas entre as principais faixas',
                            labels={'duration_min': 'Duração em Minutos'}, color_discrete_sequence=['skyblue'])
fig_duration.update_traces(marker_line_color='black', marker_line_width=1.5)

st.plotly_chart(fig_duration, use_container_width=True)

st.write('Através do histograma das durações das músicas, é possível entender como se distribuem as durações das faixas mais populares, o que pode refletir tanto a norma de produção musical quanto a preferência dos ouvintes por músicas mais curtas ou mais longas.')
st.divider()
st.subheader('Como a energia de uma faixa se relaciona com o seu volume?')


# Create a Plotly scatter plot for the relationship between energy and loudness
fig_energy_loudness = px.scatter(df, x='energy', y='loudness', opacity=0.4,
                                 title='Relacionamento entre Energia e Volume das Faixas',
                                 labels={'energy': 'Energia', 'loudness': 'Volume (dB)'})
st.plotly_chart(fig_energy_loudness, use_container_width=True)

st.write('O gráfico de dispersão entre energia e volume das faixas mostra como essas características se correlacionam. Geralmente, faixas mais energéticas tendem a ser mais altas. Esta relação é útil para entender como características técnicas da música se interligam para criar diferentes experiências auditivas.')
st.divider()
st.subheader('Qual é o nível médio de energia dentro dos 5 gêneros mais comuns?')
# Assuming df_novo is the same as df and using df for this calculation
top_5_genres = df['genre'].value_counts().head(5).index.tolist()
df_top_5_genres = df[df['genre'].isin(top_5_genres)]
df_teste = df_top_5_genres.groupby('genre').agg({'energy':'mean'})

# Create a Plotly bar chart for the average energy level within the top 5 genres
fig_top_5_genres = px.bar(df_teste, x=df_teste.index, y='energy',
                          labels={'energy': 'Energia Média', 'genre': 'Gênero'}, color=df_teste.index,
                          title='Nível médio de energia dentro dos 5 gêneros mais comuns')
st.plotly_chart(fig_top_5_genres, use_container_width=True)

st.write('Este gráfico de barras mostra a energia média nos cinco gêneros mais comuns, fornecendo uma visão sobre quais gêneros tendem a ser mais energéticos. Isso pode ajudar artistas e produtores a alinhar suas criações com as expectativas dos ouvintes nesses gêneros.')























