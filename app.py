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
st.sidebar.markdown("<br><br><br><br><br>", unsafe_allow_html=True)  # Adiciona espaços

# Créditos refinados na barra lateral
st.sidebar.markdown("**🔹 Créditos**")
st.sidebar.text("👨‍💻 Alunos: Thiago Félix, Pedro Guimarães")
st.sidebar.text("👨‍🏫 Professor orientador: Alexandre Roriz")
st.sidebar.text("📅 Ano dos dados analisados: 2018-2022")
