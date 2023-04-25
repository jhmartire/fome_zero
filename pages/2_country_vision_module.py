
#====================================================================================================
#  LIBRARIES
#====================================================================================================

import pandas               as pd
import numpy                as np
import plotly.express       as px
import plotly.graph_objects as go
import seaborn              as sns
import streamlit            as st
import inflection
import folium
from PIL                    import Image
from folium.plugins         import MarkerCluster
from matplotlib             import pyplot as plt
from streamlit_folium       import folium_static
#====================================================================================================
# FUNÇÕES
#====================================================================================================

# Renomear e padronizar as colunas

def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new

    return df

# Nomear os países por meio do código

COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}

def country_name(country_id):
    return COUNTRIES[country_id]

# Categorizar os intervalos de preço

def create_price_tye(price_range):
    if price_range == 1:
        return "Cheap"
    elif price_range == 2:
        return "Normal"
    elif price_range == 3:
        return "Expensive"
    else:
        return "Gourmet"

# Nomear as colunas por meio de código
COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}

def color_name(color_code):
    return COLORS[color_code]

#====================================================================================================
# LOADING FILE
#====================================================================================================
df = pd.read_csv('dataset/zomato.csv')

def clean_code(df):

    df1 = df.copy()

    # Renomeando os arquivos
    df1 = rename_columns(df)

    # Criação de colunas
    df1['country'] = df1.loc[:,'country_code'].apply(lambda x: country_name(x))
    df1['price_type'] = df1.loc[:, 'price_range'].apply(lambda x: create_price_tye(x))
    df1['color'] = df1.loc[:, 'rating_color'].apply(lambda x: color_name(x))

    # Pegando apenas o primeiro elemento do tipo de cozinha
    df1 = df1.loc[df1['cuisines'].notnull(), :]
    df1['cuisines'] = df1.loc[:, 'cuisines'].astype(str).apply(lambda x: x.split(',')[0])

    # Removendo colunas desnecessárias
    df1 = df1.drop(columns = ['country_code','locality_verbose', 'switch_to_order_menu','rating_color'])

    # Removendo dados duplicados, entre outros
    df1 = df1.drop_duplicates(subset='restaurant_id', keep='first')
    df1 = df1.loc[df1['average_cost_for_two'] != 0, :]

    # Resetando o index
    df1 = df1.reset_index(drop = True)
    
    return df1

df1 = clean_code(df)
df1.head()
# Gráfico de barras

def bar_graph (data, x, y, color, text):
    
    plt.figure(figsize = (20,15))
    fig = px.bar(data, x=x, y=y, template='plotly_white', color=color,
           color_continuous_scale='YlGnBu', text=text)
    fig.update(layout_showlegend=False)
    fig.update_traces(textangle=0, textposition='outside')
    
    return fig

# Gráfico treemap

def treemap_graph(data, path, value, color):
    
    fig = px.treemap(data, path=[path], values=value, color = color, color_continuous_scale = 'RdBu',
           template ='plotly_white')
    fig.data[0].texttemplate = "<b>%{label}</b><br>Qt. Culinárias: %{value}<br>"
    
    return fig
#====================================================================================================
# SIDEBAR - Topo
#====================================================================================================
st.set_page_config(page_title='Home',
                   layout="wide",
                   page_icon=':bar_chart:')

st.header ('Fome Zero')
st.header ('The best place to find your newest favorite restaurant!')

st.subheader ('We have the following brands within our platform:')

# Barra Lateral: Cabeçalho - Logo e nome da empresa
image_path = 'logo.png'
image = Image.open(image_path)
st.sidebar.image(image)

st.sidebar.markdown ("<h3 style='text-align: center; color: red;'> World Gastronomic Best Experiences</h3>", unsafe_allow_html=True)
st.sidebar.markdown ('''___''')

#====================================================================================================
# FILTROS SIDEBAR
#====================================================================================================

st.sidebar.markdown ('# Filtros')

# País
paises = list (df1['country'].unique())
country_options = st.sidebar.multiselect('Selecione os países: ', paises, default = paises)

#====================================================================================================
# Habilidatação dos filtros
#====================================================================================================

# Filtro País

linhas = df1['country'].isin(country_options)
df1 = df1.loc[linhas, :]

#====================================================================================================
# SIDEBAR - Final
#====================================================================================================
st.sidebar.markdown ('''___''')
st.sidebar.markdown ('###### Powered by Comunidade DS')
st.sidebar.markdown ('###### Data Analyst: Joao Martire')

#====================================================================================================
# Layout - Country Vision 
#====================================================================================================

with st.container():
    
    st.markdown('### Quantidade de restaurantes por país')
    
    contagem = df1[['restaurant_id', 'country']].groupby('country').count().sort_values('restaurant_id', ascending = True).reset_index()
    contagem.columns = ['Países', 'Qt. Restaurantes']

    fig = bar_graph(contagem, x='Países', y='Qt. Restaurantes', color='Países', text='Qt. Restaurantes')
    st.plotly_chart(fig, use_container_width = True, theme='streamlit')
    
with st.container():
    
    st.markdown('### Quantidade de cidades por país')
    
    contagem = df1[['city', 'country']].groupby('country').nunique().sort_values('city', ascending = True).reset_index()
    contagem.columns = ['Países', 'Qt. Cidades']

    fig = bar_graph(contagem, x='Países', y='Qt. Cidades', color='Países', text='Qt. Cidades')
    st.plotly_chart(fig, use_container_width = True, theme='streamlit')

with st.container():
    
    col1, col2 = st.columns(2)
    
    with col1:
        
        st.markdown('#### Diversidade Gastronômica: ')
        st.markdown('###### Quantidade de culinárias únicas por país')
        
        contagem = df1[['country','cuisines']].groupby('country').nunique().sort_values('cuisines', ascending = False).reset_index()
        contagem.columns=['País','Culinárias']

        fig = treemap_graph(contagem, path='País', value='Culinárias', color='Culinárias')
        st.plotly_chart(fig, use_container_width = True, theme='streamlit')
         
    with col2:
        
        st.markdown('#### Top 5 Países com maior quantitativo de avaliações')
        
        contagem = df1[['country', 'votes']].groupby('country').sum().sort_values('votes', ascending = False).reset_index().head(5)
        contagem.columns = ['Países', 'Qt. Avaliações (Milhões)']
        
        fig= bar_graph(contagem, x='Qt. Avaliações (Milhões)', y='Países', color='Países', text='Qt. Avaliações (Milhões)')
        fig.update_traces(textposition=None)
        st.plotly_chart(fig, use_container_width = True, theme='streamlit')
        
with st.container():
    
    col1, col2 = st.columns(2)
    
    with col1:
        
        st.markdown('#### Avaliação média por país')
        
        contagem = df1[['country', 'aggregate_rating']].groupby('country').mean().sort_values('aggregate_rating', ascending = True).reset_index()
        contagem.columns=['Países', 'Média das Avaliações']

        fig = bar_graph (contagem, x='Países', y='Média das Avaliações', color ='Países', text='Média das Avaliações')
        fig.update_traces(textangle=0, textposition='inside', texttemplate='%{text:.2f}')
        st.plotly_chart(fig, use_container_width = True, theme='streamlit')

    with col2:
   
        st.markdown('#### Média de custo e de avaliação dos países')
        linhas = ((df1['price_type'] == 'Expensive') | (df1['price_type'] == 'Gourmet')) & (df1['aggregate_rating'] < 2.5)
        contagem = df1.loc[linhas, ['country', 'city','average_cost_for_two', 'aggregate_rating']].groupby('city').mean(['average_cost_for_two', 'aggregate_rating']).sort_values('aggregate_rating', ascending = True).reset_index().head(10)
        df2 = df1[['country', 'city', 'currency']].drop_duplicates(subset='city', keep='first')

        df3 = pd.merge(df2, contagem, how='inner')
        df3 = df3.sort_values('aggregate_rating', ascending = True).reset_index(drop=True)
        df3.columns = ['País', 'Cidade', 'Moeda', 'Preço Médio - Prato p/ 2', 'Média Avaliativa']
        st.dataframe(df3.style.format(subset=['Preço Médio - Prato p/ 2', 'Média Avaliativa'], formatter="{:.2f}"))

    
















