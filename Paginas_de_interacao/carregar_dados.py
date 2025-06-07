import pandas as pd
import streamlit as st

@st.cache_data
def carregar_dados():
    dados = pd.read_csv("dados_senso_padronizado.csv",sep=';')
    # Se quiser já tratar algo, pode fazer aqui
    return dados
