import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. Configuração de Estilo e Página
st.set_page_config(page_title="Mayhem: Eternal Ritual", layout="wide")

# CSS para Fundo Preto Total, Tabela de Sangue e Estilo do Filtro
st.markdown("""
    <style>
    .main, .stApp { background-color: #000000 !important; color: #ffffff; }
    h1, h2, h3 { color: #ff0000 !important; font-family: 'Courier New', Courier, monospace; }
    
    /* Estilização da Tabela Customizada (Red Header / Black Rows) */
    .ritual-table {
        width: 100%;
        border-collapse: collapse;
        background-color: #000000;
        color: #ffffff;
        border: 1px solid #333;
    }
    .ritual-table thead th {
        background-color: #ff0000 !important;
        color: #ffffff !important;
        padding: 12px;
        text-align: left;
        border: 1px solid #333;
        text-transform: uppercase;
    }
    .ritual-table td {
        background-color: #000000 !important;
        color: #ffffff !important;
        padding: 10px;
        border: 1px solid #333;
    }
    
    /* Estilo da 'Lupinha' de busca */
    .stTextInput > div > div > input {
        background-color: #111;
        color: white;
        border: 1px solid #ff0000;
    }
    
    /* Rodapé Estilizado */
    .footer-text {
        color: #666;
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
        padding-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Carregamento de Dados
@st.cache_data
def load_data():
    if os.path.exists("mayhem_timeline_FIXED.csv"):
        return pd.read_csv("mayhem_timeline_FIXED.csv", sep=';')
    else:
        return pd.read_excel("Mayhem_Timeline_Black_Edition.xlsx", skiprows=4)

df = load_data()
df['Ano'] = pd.to_numeric(df['Ano'], errors='coerce')

# 3. Cabeçalho (Logo à Esquerda + Título e Música)
col_logo, col_title = st.columns([1, 4])
with col_logo:
    if os.path.exists("logo.jpg"):
        st.image("logo.jpg", width=130)
with col_title:
    st.title("MAYHEM: THE TRUE BLACK METAL DASHBOARD")
    audio_file = "De Mysteriis Dom Sathanas (Live) - Mayhem (youtube).mp3"
    if os.path.exists(audio_file):
        st.audio(audio_file, format="audio/mp3")

st.divider()

# 4. Gráficos Sincronizados
c1, c2 = st.columns(2)
color_map = {'Álbum de Estúdio': '#ff0000', 'EP': '#8b0000', 'Live Album': '#4b0000', 'Demo': '#333333', 'Evento': '#ffffff'}

with c1:
    fig_pie = px.pie(df, names='Tipo', title='Proporção por Categoria',
                    color='Tipo', color_discrete_map=color_map, hole=0.4)
    fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig_pie, use_container_width=True)

with c2:
    df_counts = df['Tipo'].value_counts().reset_index()
    df_counts.columns = ['Tipo', 'Quantidade']
    fig_bar = px.bar(df_counts, x='Tipo', y='Quantidade', title='Total por Categoria',
                    color='Tipo', color_discrete_map=color_map)
    fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", showlegend=False)
    st.plotly_chart(fig_bar, use_container_width=True)

# 5. Timeline com Filtro de Busca (A Lupinha)
st.subheader("📅 Timeline da Banda")
search_term = st.text_input("🔍 Filtrar evento ou descrição:", placeholder="Ex: Dead, Euronymous, 1994...")

df_filtered = df[
    df['Evento'].str.contains(search_term, case=False, na=False) | 
    df['Descricao'].str.contains(search_term, case=False, na=False)
].sort_values('Ano')

# 6. Tabela HTML (Cabeçalho Vermelho / Linhas Pretas)
table_html = df_filtered[['Ano', 'Evento', 'Tipo', 'Gravadora', 'Descricao']].to_html(classes='ritual-table', index=False)
st.markdown(table_html, unsafe_allow_html=True)

# 7. Rodapé Finalizado
st.divider()
st.markdown('<p class="footer-text">What you found was eternal death<br>No one will ever miss you</p>', unsafe_allow_html=True)