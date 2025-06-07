import streamlit as st

def exibir():
    st.title("📉 Análise da Evasão Escolar")

    st.markdown("""
    Aqui você pode calcular e visualizar a evasão escolar. Uma forma comum de calcular é:

    ```
    evasao = 1 - (concluintes / matriculados)
    ```

    Use os gráficos e tabelas para comparar ao longo dos anos e entre grupos diferentes.
    """)