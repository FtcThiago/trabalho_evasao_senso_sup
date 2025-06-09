import streamlit as st


def exibir():
    # Título
    st.markdown("""
    <h1 style='color: #2E86C1;'>🎓 Taxas de Desistência no Ensino Superior do Distrito Federal</h1>
    <h4 style='color: #555;'>Análise baseada nos dados do Censo da Educação Superior</h4>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Propósito da Análise (Agora fora das colunas!)
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
