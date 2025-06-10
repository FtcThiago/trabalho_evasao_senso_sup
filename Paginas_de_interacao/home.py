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

    ## Objetivo da Análise
    Este estudo tem como objetivo analisar e compreender os fatores associados às taxas de desistência em cursos de graduação no Distrito Federal. A investigação será conduzida com base em dados públicos extraídos de plataformas governamentais, que abrangem informações sobre instituições de ensino superior públicas e privadas. Para fins de recorte metodológico, a amostra será composta pelas dez instituições de ensino superior do DF que obtiveram as melhores avaliações segundo o Índice Geral de Cursos (IGC) do Ministério da Educação (MEC) no ano de 2021.

    ## Justificativa
    A escolha por focar apenas nas dez instituições de ensino superior mais bem avaliadas do Distrito Federal tem como objetivo garantir maior clareza e confiabilidade na análise. Essas instituições costumam ter estruturas mais organizadas e sistemas de gestão mais transparentes, o que facilita o acesso a dados mais completos e padronizados. Além disso, ao analisar faculdades com bom desempenho, buscamos entender se a evasão estudantil também ocorre em contextos considerados positivos — o que pode apontar para questões mais amplas e estruturais no ensino superior brasileiro. Essa delimitação também está relacionada ao fato de este ser um trabalho de início de graduação, o que exige um recorte de dados menor e mais viável, sem a necessidade de incluir todas as instituições do DF ou de outros estados do país.

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

