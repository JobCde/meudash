import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import plotly.express as px

# Carregar os dados
file_path = 'C:\\teste_python\\PROJETO_EY_VALE\\SERRA_NORTE_DADOS.xlsx'
df = pd.read_excel(file_path)

# Exibir as primeiras linhas para entender a estrutura
st.write(df.head())
#%%
# Exibir as colunas para análise inicial
st.write(df.columns)

# Análise exploratória básica
# Supondo que as colunas de respondentes sejam as identificadas acima e que a coluna 'Função' e 'Área' estejam presentes
respondentes = [
    'R_11j8hQsi6cjWXGP', 'R_5X6So1KaWVhaSU9', 'R_7ltAL3jBQ8LT0Nl', 'R_8168XV6kNeqnYf4',
    'R_2oI4AeBzoFKIDiK', 'R_3nVKNV9pYTuXGAn', 'R_7PdrjLfqYFDsYex', 'R_6ULGnkOrIjIr06l',
    'R_1N3pB730iIBSPG3', 'R_3IZaW7ejNEtYpwW', 'R_7mOxbfeluKROnYX', 'R_7gLAyYbbzABCJk5'
]

# Identificar as colunas de interesse
col_questoes = 'Coluna_Questao'  # Substitua com o nome correto da coluna
col_sku = 'Coluna_SKU'  # Substitua com o nome correto da coluna
col_funcao = 'Função'  # Substitua com o nome correto da coluna
col_area = 'Área'  # Substitua com o nome correto da coluna

# Mostrando a distribuição das notas para uma questão específica
questao_selecionada = st.selectbox('Selecione uma questão:', df[col_questoes].unique())

# Filtrando o DataFrame para a questão selecionada
df_questao = df[df[col_questoes] == questao_selecionada]

# Mostrar as respostas dos respondentes
st.write(df_questao[respondentes])

# Gráfico de barras para distribuição das notas
st.bar_chart(df_questao[respondentes].mean())

# Nuvem de palavras para os comentários (se houver)
if 'Comentários' in df.columns:
    comentarios = ' '.join(df_questao['Comentários'].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(comentarios)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

# Filtragem por função e área
funcao_selecionada = st.selectbox('Selecione uma função:', df[col_funcao].unique())
area_selecionada = st.selectbox('Selecione uma área de atuação:', df[col_area].unique())

df_filtrado = df_questao[(df[col_funcao] == funcao_selecionada) & (df[col_area] == area_selecionada)]

# Exibir resultados filtrados
st.write(df_filtrado)
