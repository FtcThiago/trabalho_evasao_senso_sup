import streamlit as st

def exibir():
    st.title("📊 Dashboard Interativo")
    st.markdown("Aqui o usuário pode escolher filtros e gerar os próprios gráficos.")
    
    st.warning("🔧 Você ainda precisa implementar os filtros e gráficos aqui.")

   
    # Geral
    with st.expander("🔹 Geral"):
        dados_agrupados = dados.groupby('NU_ANO_CENSO').sum()
        fig = go.Figure()
        fig.add_trace(go.Bar(x=dados_agrupados.index, y=dados_agrupados["QT_MAT"], name="Matriculados"))
        fig.add_trace(go.Bar(x=dados_agrupados.index, y=dados_agrupados["QT_CONC"], name="Concluintes"))
        fig.update_layout(title="Geral - Matriculados x Concluintes", barmode="group")
        st.plotly_chart(fig)
        st.dataframe(dados_agrupados[["QT_MAT", "QT_CONC"]])

    # Masculino
    with st.expander("🔹 Sexo Masculino"):
        dados_masc = dados.groupby("NU_ANO_CENSO")[["QT_MAT_MASC", "QT_CONC_MASC"]].sum()
        fig = go.Figure()
        fig.add_trace(go.Bar(x=dados_masc.index, y=dados_masc["QT_MAT_MASC"], name="Matriculados"))
        fig.add_trace(go.Bar(x=dados_masc.index, y=dados_masc["QT_CONC_MASC"], name="Concluintes"))
        fig.update_layout(title="Masculino - Matriculados x Concluintes", barmode="group")
        st.plotly_chart(fig)
        st.dataframe(dados_masc)

    # Feminino
    with st.expander("🔹 Sexo Feminino"):
        dados_fem = dados.groupby("NU_ANO_CENSO")[["QT_MAT_FEM", "QT_CONC_FEM"]].sum()
        fig = go.Figure()
        fig.add_trace(go.Bar(x=dados_fem.index, y=dados_fem["QT_MAT_FEM"], name="Matriculados"))
        fig.add_trace(go.Bar(x=dados_fem.index, y=dados_fem["QT_CONC_FEM"], name="Concluintes"))
        fig.update_layout(title="Feminino - Matriculados x Concluintes", barmode="group")
        st.plotly_chart(fig)
        st.dataframe(dados_fem)