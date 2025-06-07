import streamlit as st
import pandas as pd
from datetime import date
from Paginas_de_interacao.Perguntas import mostrar_perguntas

dados_senso = pd.read_csv("Projeot_censo_ed_streamlit\\trabalho_evasao_senso_sup\\dados_senso_padronizado.csv",sep=';')




# ----------------------
# Configuração da página
# ----------------------
st.set_page_config(
    page_title="Análise Exploratória de Dados - Projeto Final",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------
# Menu lateral (abas)
# ----------------------
menu = st.sidebar.radio("Navegação", ["📘 Introdução", "🔍 Perguntas & Análises", "📊 Gráficos", "📁 Conclusão"])

# ----------------------
# Página: Introdução
# ----------------------
if menu == "📘 Introdução":
    st.title("📊 Análise Exploratória de Dados")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎓 Informações do Trabalho")
        st.markdown("""
        **Disciplina:** Análise de Dados  
        **Objetivo:** Aplicar conceitos de Análise Exploratória de Dados em um conjunto real  
        **Entrega:** `05/06/2025`  
        """)
    
    with col2:
        st.subheader("👥 Autoria")
        st.markdown("""
        **Aluno:** Thiago Félix
                    
        **Aluno:** Pedro Guimaraes
                    
        **Professor:** Alexandre ***   
        """)
    
    st.markdown("---")
    st.write("### 📌 Apresentação do Projeto")
    st.write("""
    Este projeto consiste na exploração de um conjunto de dados de livre escolha, com o objetivo de levantar perguntas relevantes,
    interpretar os resultados e expressar os achados por meio de gráficos e análises comentadas.
    
    A seguir, você poderá navegar entre as abas laterais para visualizar os dados, as perguntas feitas, os gráficos construídos e a conclusão do trabalho.
    """)
    st.info("Utilize o menu lateral para navegar entre as seções.", icon="📚")

# ----------------------
# Página: Perguntas & Análises
# ----------------------
elif menu == "🔍 Perguntas & Análises":
    mostrar_perguntas()

# ----------------------
# Página: Gráficos
# ----------------------
elif menu == "📊 Gráficos":
    st.header("📊 Visualizações e Gráficos")
    st.write("Utilize esta seção para apresentar gráficos que representem suas descobertas de forma clara.")
    
    # Exemplo de gráfico com matplotlib (pode trocar pelo que quiser)
    import matplotlib.pyplot as plt
    import numpy as np
    
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.plot(x, y)
    ax.set_title("Exemplo de Gráfico")
    st.pyplot(fig)

# ----------------------
# Página: Conclusão
# ----------------------
elif menu == "📁 Conclusão":
    st.header("📁 Conclusão do Projeto")
    st.markdown("""
    Aqui você pode escrever um resumo das descobertas feitas com a análise dos dados.
    
    - Quais foram os padrões interessantes?
    - Houve algo inesperado?
    - O que essa análise pode ajudar a responder na prática?
    - Sugestões para próximos passos ou estudos.
    """)

