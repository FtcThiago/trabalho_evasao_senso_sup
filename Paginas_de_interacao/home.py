import streamlit as st

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
        st.image("Imagem/home_2.jpeg", use_container_width=True)

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
