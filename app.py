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
st.sidebar.markdown("""
    <div style="background-color: #2E86C1; padding: 10px; border-radius: 8px;">
        <h3 style="color: white; text-align: center;">🔹 Créditos 🔹</h3>
    </div>
    <br>
    <p style="font-size: 16px;"><strong>👨‍💻 Alunos:</strong> Thiago Félix, Pedro Guimarães</p>
    <p style="font-size: 16px;"><strong>👨‍🏫 Professor orientador:</strong> Alexandre Roriz</p>
    <p style="font-size: 16px;"><strong>📅 Ano dos dados analisados:</strong> 2018-2022</p>
""", unsafe_allow_html=True)
