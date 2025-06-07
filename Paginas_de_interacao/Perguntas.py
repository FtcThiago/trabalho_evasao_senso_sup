import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from Paginas_de_interacao.carregar_dados import carregar_dados

dados = carregar_dados()

def mostrar_perguntas():
    st.header("🔍 Perguntas Investigativas e Respostas")
    st.markdown("Abaixo estão as perguntas elaboradas com base nos dados e suas respectivas análises.")

    # Exemplo de Pergunta 1
    with st.expander("🔸 1. Quantos alunos ingressaram e quantos se formaram?"):
        st.markdown("**Pergunta:** 1. Quantos alunos ingressaram e quantos se formaram?")
        
        # Lógica de análise
        dados_agrupados = dados.groupby('NU_ANO_CENSO').sum()

        # Agrupando os dados por ano
        dados_agrupados = dados.groupby('NU_ANO_CENSO').sum()

        # 🔹 Gráfico Geral
        fig_geral = go.Figure()
        fig_geral.add_trace(go.Bar(x=dados_agrupados.index, y=dados_agrupados["QT_MAT"], name="Matriculados"))
        fig_geral.add_trace(go.Bar(x=dados_agrupados.index, y=dados_agrupados["QT_CONC"], name="Concluintes"))
        fig_geral.update_layout(
            title="Matriculados & Concluintes - Geral",
            xaxis_title="Ano",
            yaxis_title="Quantidade",
            barmode="group",
            template="plotly_white"
        )



        st.markdown("**Resposta:** A média de idade varia entre as classes. A 1ª classe tem a maior média, sugerindo que passageiros mais velhos tinham mais condições de pagar por conforto.")
        st.markdown("**Comentário:** Isso pode indicar uma correlação entre idade e poder aquisitivo no contexto da época.")

    # Exemplo de Pergunta 2
    with st.expander("🔸 Pergunta 2: Qual a proporção de sobreviventes por sexo?"):
        st.markdown("**Pergunta:** Qual a proporção de sobreviventes por sexo?")

       

        st.markdown("**Resposta:** Mulheres tiveram uma taxa de sobrevivência muito maior que os homens.")
        st.markdown("**Comentário:** Isso pode ser explicado pela política 'mulheres e crianças primeiro' durante o naufrágio.")
        
