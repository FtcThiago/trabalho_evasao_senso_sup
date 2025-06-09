import streamlit as st
import numpy as np
import matplotlib as plt

def exibir():
 
    # Título com destaque
    st.markdown("""
    <h1 style='text-align: center; color: #2E86C1;'>🎓 Taxas de Desistência no Ensino Superior do Distrito Federal</h1>
    <h4 style='text-align: center; color: #555;'>Análise baseada nos dados do Censo da Educação Superior</h4>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Container central
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        x = np.linspace(1, 12, 12)  # Meses do ano
        y = np.random.randint(20, 80, size=12)  # Valores fictícios

        # Criando a figura
        fig, ax = plt.subplots(figsize=(12, 4))  # Ajusta largura e altura

        ax.plot(x, y, color='#8000FF', linewidth=2, marker='o', markersize=8, label="Taxa de evasão")

        # Personalizando o gráfico
        ax.set_facecolor("black")  # Fundo preto
        ax.tick_params(colors='white')  # Eixos em branco
        ax.set_title("Evasão Escolar ao Longo do Ano", fontsize=14, color='white')
        ax.set_xlabel("Mês", fontsize=12, color='white')
        ax.set_ylabel("Taxa (%)", fontsize=12, color='white')
        ax.legend(facecolor="black", edgecolor="white", fontsize=12)

        # Exibir no Streamlit
        st.pyplot(fig)


    # Propósito da Análise
    st.markdown("""
    ## 🎯 Propósito da Análise

    Este projeto tem como objetivo compreender os fatores relacionados à **evasão no ensino superior** do Distrito Federal.

    Através dos dados públicos do Censo da Educação Superior, buscamos responder perguntas como:

    - Quantos alunos ingressaram e quantos se formaram ao longo dos anos?
    - Existe diferença de evasão entre cursos noturnos e diurnos?
    - A evasão varia entre faixas etárias?
    - A cor/raça influencia na taxa de evasão?
    - Alunos com deficiência têm maior evasão?
    - A evasão é diferente entre cursos de áreas diferentes?
    - A evasão é maior em cursos EAD?
    - Qual é a distribuição racial dos estudantes em cada área do ensino superior?


    """)

    # Créditos
    st.markdown("---")
    st.markdown("""
    👨‍💻 **Alunos:** Thiago Félix, Pedro Guimarães  
    👨‍🏫 **Professor orientador:** Alexandre Roriz  
    📅 **Ano dos dados analisados:** 2018-2022
    """)

    # Chamada final
    st.markdown("---")
    st.markdown("""
    <h2>👨‍💻 <b>Alunos:</b> Thiago Félix, Pedro Guimarães</h2>
    <h2>👨‍🏫 <b>Professor orientador:</b> Alexandre Roriz</h2>
    <h2>📅 <b>Ano dos dados analisados:</b> 2018-2022</h2>
""", unsafe_allow_html=True)
