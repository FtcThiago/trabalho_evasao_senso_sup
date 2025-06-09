
import streamlit as st
import pandas as pd
import plotly.express as px


from Paginas_de_interacao.carregar_dados import carregar_dados

dados = carregar_dados()


def exibir():
    # 2. Sidebar: Filtros e Opções de Detalhamento
    # =============================================================================
    st.sidebar.header("Filtros Gerais")

    curso_selecionado = st.sidebar.selectbox(
        "Curso Detalhado", sorted(dados["NO_CINE_AREA_DETALHADA"].unique())
    )
    ano_selecionado = st.sidebar.selectbox(
        "Ano do Censo", sorted(dados["NU_ANO_CENSO"].unique())
    )
    opcao_genero = st.sidebar.radio(
        "Visualizar dados:", ["Geral", "Somente Homens", "Somente Mulheres"]
    )
    detalhamento_opcao = st.sidebar.radio(
        "Detalhamento", ["Detalhamento (Texto)", "Visual (Gráficos)"]
    )

    # =============================================================================
    # 3. Filtrar e Agregar os Dados
    # =============================================================================
    dados_filtrados = dados[
        (dados["NO_CINE_AREA_DETALHADA"] == curso_selecionado) &
        (dados["NU_ANO_CENSO"] == ano_selecionado)
    ]

    if not dados_filtrados.empty:
        dados_agregados = dados_filtrados.groupby("NO_CINE_AREA_DETALHADA").sum().reset_index()
    else:
        dados_agregados = pd.DataFrame()

    # =============================================================================
    # 4. Cálculo dos Indicadores – considerando a opção de gênero
    # =============================================================================
    # Se "Geral", usamos os totais; se "Somente Homens" ou "Somente Mulheres", usamos as colunas correspondentes.
    if opcao_genero == "Geral":
        mat_total   = dados_agregados["QT_MAT"].iloc[0]
        conc_total  = dados_agregados["QT_CONC"].iloc[0]
        mat_homens  = dados_agregados["QT_MAT_MASC"].iloc[0]
        conc_homens = dados_agregados["QT_CONC_MASC"].iloc[0]
        mat_mulheres  = dados_agregados["QT_MAT_FEM"].iloc[0]
        conc_mulheres = dados_agregados["QT_CONC_FEM"].iloc[0]
        indicador_label = "Geral"
    elif opcao_genero == "Somente Homens":
        mat_total  = dados_agregados["QT_MAT_MASC"].iloc[0]
        conc_total = dados_agregados["QT_CONC_MASC"].iloc[0]
        indicador_label = "Homens"
    else:  # Somente Mulheres
        mat_total  = dados_agregados["QT_MAT_FEM"].iloc[0]
        conc_total = dados_agregados["QT_CONC_FEM"].iloc[0]
        indicador_label = "Mulheres"

    # Taxa de Evasão (%)
    taxa_evasao = round(((mat_total - conc_total) / mat_total) * 100, 2) if mat_total > 0 else 0

    # =============================================================================
    # 5. Apresentação do Detalhamento
    # =============================================================================
    st.title(f"Detalhamento para {curso_selecionado} ({ano_selecionado})")

    if detalhamento_opcao == "Detalhamento (Texto)":
        st.markdown("## Indicadores Gerais")
        st.markdown(f"**Matrículas Totais ({indicador_label}):** {mat_total:,}")
        st.markdown(f"**Conclusões Totais ({indicador_label}):** {conc_total:,}")
        st.markdown(f"**Taxa de Evasão:** {taxa_evasao}%")
        
        if opcao_genero == "Geral":
            st.markdown("### Dados por Gênero")
            st.markdown(f"- **Matrículas Homens:** {mat_homens:,} | **Conclusões Homens:** {conc_homens:,}")
            st.markdown(f"- **Matrículas Mulheres:** {mat_mulheres:,} | **Conclusões Mulheres:** {conc_mulheres:,}")
            
        st.markdown("## Distribuição Racial (Matrículas)")
        st.markdown(f"- **Branca:** {dados_agregados['QT_MAT_BRANCA'].iloc[0]:,}")
        st.markdown(f"- **Preta:** {dados_agregados['QT_MAT_PRETA'].iloc[0]:,}")
        st.markdown(f"- **Parda:** {dados_agregados['QT_MAT_PARDA'].iloc[0]:,}")
        st.markdown(f"- **Amarela:** {dados_agregados['QT_MAT_AMARELA'].iloc[0]:,}")
        st.markdown(f"- **Indígena:** {dados_agregados['QT_MAT_INDIGENA'].iloc[0]:,}")
        st.markdown(f"- **Cornd:** {dados_agregados['QT_MAT_CORND'].iloc[0]:,}")
        
        st.markdown("## Distribuição por Faixa Etária (Matrículas)")
        st.markdown(f"- **0-17:** {dados_agregados['QT_MAT_0_17'].iloc[0]:,}")
        st.markdown(f"- **18-24:** {dados_agregados['QT_MAT_18_24'].iloc[0]:,}")
        st.markdown(f"- **25-29:** {dados_agregados['QT_MAT_25_29'].iloc[0]:,}")
        st.markdown(f"- **30-34:** {dados_agregados['QT_MAT_30_34'].iloc[0]:,}")
        st.markdown(f"- **35-39:** {dados_agregados['QT_MAT_35_39'].iloc[0]:,}")
        st.markdown(f"- **40-49:** {dados_agregados['QT_MAT_40_49'].iloc[0]:,}")
        st.markdown(f"- **50-59:** {dados_agregados['QT_MAT_50_59'].iloc[0]:,}")
        st.markdown(f"- **60+:** {dados_agregados['QT_MAT_60_MAIS'].iloc[0]:,}")
        
        st.markdown("## Outras Informações")
        st.markdown(f"- **Modalidade de Ensino:** {dados_agregados['TP_MODALIDADE_ENSINO'].iloc[0]}")
        st.markdown(f"- **Nível Acadêmico:** {dados_agregados['TP_NIVEL_ACADEMICO'].iloc[0]}")
        st.markdown(f"- **Matrículas Diurnas:** {dados_agregados['QT_MAT_DIURNO'].iloc[0]:,} | **Noturnas:** {dados_agregados['QT_MAT_NOTURNO'].iloc[0]:,}")
        st.markdown(f"- **Deficientes - Matrículas:** {dados_agregados['QT_MAT_DEFICIENTE'].iloc[0]:,} | **Conclusões:** {dados_agregados['QT_CONC_DEFICIENTE'].iloc[0]:,}")
        st.markdown(f"- **Não Estrangeiro - Matrículas:** {dados_agregados['QT_MAT_NACESTRANG'].iloc[0]:,} | **Conclusões:** {dados_agregados['QT_CONC_NACESTRANG'].iloc[0]:,}")
        st.markdown(f"- **Processo Seletivo Pública:** Matrículas {dados_agregados['QT_MAT_PROCESCPUBLICA'].iloc[0]:,} | Conclusões {dados_agregados['QT_CONC_PROCESCPUBLICA'].iloc[0]:,}")
        st.markdown(f"- **Processo Seletivo Privada:** Matrículas {dados_agregados['QT_MAT_PROCESCPRIVADA'].iloc[0]:,} | Conclusões {dados_agregados['QT_CONC_PROCESCPRIVADA'].iloc[0]:,}")
        st.markdown(f"- **Financiamento:** Matrículas {dados_agregados['QT_MAT_FINANC'].iloc[0]:,} | Conclusões {dados_agregados['QT_CONC_FINANC'].iloc[0]:,}")
        
    else:
        # =============================================================================
        # 6. Detalhamento Visual (Gráficos) – agora fazendo com que, se "Somente Homens" ou "Somente Mulheres"
        # sejam escolhidos, o gráfico 1 utiliza os dados corretos.
        # =============================================================================
        st.subheader("Detalhamento Visual")
        
        # Preparar os valores específicos para o gráfico Comparativo de Matrículas vs. Conclusões
        if opcao_genero == "Geral":
            valor_mat = dados_agregados["QT_MAT"].iloc[0]
            valor_conc = dados_agregados["QT_CONC"].iloc[0]
            label_mat = "Matrículas Totais"
            label_conc = "Conclusões Totais"
        elif opcao_genero == "Somente Homens":
            valor_mat = dados_agregados["QT_MAT_MASC"].iloc[0]
            valor_conc = dados_agregados["QT_CONC_MASC"].iloc[0]
            label_mat = "Matrículas Homens"
            label_conc = "Conclusões Homens"
        else:  # Somente Mulheres
            valor_mat = dados_agregados["QT_MAT_FEM"].iloc[0]
            valor_conc = dados_agregados["QT_CONC_FEM"].iloc[0]
            label_mat = "Matrículas Mulheres"
            label_conc = "Conclusões Mulheres"

        col1, col2 = st.columns(2)
        
        # Gráfico 1: Comparação de Matrículas vs. Conclusões (usando os valores filtrados por gênero)
        with col1:
            fig_mat_conc = px.bar(
                x=[label_mat, label_conc],
                y=[valor_mat, valor_conc],
                labels={"x": "Indicador", "y": "Quantidade"},
                title="Comparação de Matrículas vs. Conclusões"
            )
            st.plotly_chart(fig_mat_conc, use_container_width=True)
        
        # Gráfico 2: Distribuição Racial (usando os totais agregados, já que as colunas não são segregadas por gênero)
        with col2:
            racas = {
                "Branca": dados_agregados["QT_MAT_BRANCA"].iloc[0],
                "Preta": dados_agregados["QT_MAT_PRETA"].iloc[0],
                "Parda": dados_agregados["QT_MAT_PARDA"].iloc[0],
                "Amarela": dados_agregados["QT_MAT_AMARELA"].iloc[0],
                "Indígena": dados_agregados["QT_MAT_INDIGENA"].iloc[0],
                "Cornd": dados_agregados["QT_MAT_CORND"].iloc[0]
            }
            df_racas = pd.DataFrame(list(racas.items()), columns=["Raça", "Matrículas"])
            fig_racas = px.pie(df_racas, names="Raça", values="Matrículas", title="Distribuição Racial")
            st.plotly_chart(fig_racas, use_container_width=True)
        
        # Gráfico 3: Distribuição por Faixa Etária (Matrículas)
        st.subheader("Distribuição por Faixa Etária")
        faixa_etaria = {
            "0-17": dados_agregados["QT_MAT_0_17"].iloc[0],
            "18-24": dados_agregados["QT_MAT_18_24"].iloc[0],
            "25-29": dados_agregados["QT_MAT_25_29"].iloc[0],
            "30-34": dados_agregados["QT_MAT_30_34"].iloc[0],
            "35-39": dados_agregados["QT_MAT_35_39"].iloc[0],
            "40-49": dados_agregados["QT_MAT_40_49"].iloc[0],
            "50-59": dados_agregados["QT_MAT_50_59"].iloc[0],
            "60+": dados_agregados["QT_MAT_60_MAIS"].iloc[0]
        }
        df_faixa = pd.DataFrame(list(faixa_etaria.items()), columns=["Faixa Etária", "Matrículas"])
        fig_faixa = px.bar(df_faixa, x="Faixa Etária", y="Matrículas", title="Distribuição por Faixa Etária")
        st.plotly_chart(fig_faixa, use_container_width=True)
