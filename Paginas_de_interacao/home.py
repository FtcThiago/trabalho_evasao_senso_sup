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
        st.image("Imagem/imagem_home.png", use_column_width=True)

    # Propósito da Análise
    st.markdown("""
    ## 🎯 Propósito da Análise

    Este projeto tem como objetivo compreender os fatores relacionados à **evasão no ensino superior** do Distrito Federal.

    Através dos dados públicos do Censo da Educação Superior, buscamos responder perguntas como:

    - Quais cursos apresentam **maior taxa de desistência**?
    - Há diferença de evasão entre **turnos, sexos e raças**?
    - A **modalidade de ensino (presencial vs EAD)** influencia na permanência?
    - Como variáveis como **idade, rede e financiamento** impactam a conclusão do curso?

    """)

    # Créditos
    st.markdown("---")
    st.markdown("""
    👨‍💻 **Alunos:** Thiago Félix, Pedro Guimarães  
    👨‍🏫 **Professor orientador:** Alexandre Roriz  
    📅 **Ano dos dados analisados:** 2018-2022
    """)

    # Chamada final
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <h4 style='text-align: center;'>📊 Explore os dados nas páginas laterais e descubra os padrões por trás das taxas de desistência!</h4>
    """, unsafe_allow_html=True)
