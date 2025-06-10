import streamlit as st
st.set_page_config(page_title="Análise Educacional", layout="wide")

from Paginas_de_interacao import home, Perguntas, evasao, dashboard, conclusao, sobre, carregar_dados

# Menu lateral
menu = st.sidebar.selectbox("Navegue pelas seções:", [
    "🏠 Página Inicial",
    "❓ Perguntas Investigativas",
    "📉 Análise da Evasão",
    "📊 Dashboard Interativo",
    "🧠 Conclusões",
    "📁 Sobre os Dados"
])

# Renderização condicional das páginas
if menu == "🏠 Página Inicial":
    home.exibir()
elif menu == "❓ Perguntas Investigativas":
    Perguntas.exibir()
elif menu == "📉 Análise da Evasão":
    evasao.exibir()
elif menu == "📊 Dashboard Interativo":
    dashboard.exibir()
elif menu == "🧠 Conclusões":
    conclusao.exibir()
elif menu == "📁 Sobre os Dados":
    sobre.exibir()

# Créditos no menu lateral abaixo
st.sidebar.markdown("---")
st.sidebar.markdown("""
👨‍💻 **Alunos:** Thiago Félix, Pedro Guimarães  
👨‍🏫 **Professor orientador:** Alexandre Roriz  
📅 **Ano dos dados analisados:** 2018-2022
""")