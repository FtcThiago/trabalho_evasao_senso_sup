import streamlit as st

def exibir():
    st.title("📁 Sobre os Dados")
    st.markdown("""
    - **Fonte:** Censo da Educação Superior (INEP) ou outro
    - **Descrição das colunas principais:**
      - `NU_ANO_CENSO`: Ano
      - `QT_MAT`: Quantidade de matriculados
      - `QT_CONC`: Quantidade de concluintes
      - ...

    - **Tratamentos feitos:** limpeza, preenchimento de nulos, etc.
    """)