import pandas as pd
import streamlit as st
import os

@st.cache_data
def carregar_dados():
    caminho_base = os.path.dirname(__file__)
    caminho_csv = os.path.join(caminho_base, "..", "dados_senso_padronizado.csv")  # Volta um nível
    return pd.read_csv(caminho_csv, sep=';')
