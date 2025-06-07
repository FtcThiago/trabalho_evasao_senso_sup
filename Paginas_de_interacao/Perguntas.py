import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from Paginas_de_interacao.carregar_dados import carregar_dados

dados = carregar_dados()

def exibir():
    with st.expander("🔹1. Quantos alunos ingressaram e quantos se formaram ao longo dos anos?"):
        st.subheader("🔹1. Quantos alunos ingressaram e quantos se formaram ao longo dos anos?")

        opcoes = {
            "Geral": {
                "mat": "QT_MAT",
                "conc": "QT_CONC",
                "titulo": "Geral - Matriculados x Concluintes",
                "cor_mat": "#1f77b4",   # Azul
                "cor_conc": "#2ca02c"   # Verde
            },
            "Masculino": {
                "mat": "QT_MAT_MASC",
                "conc": "QT_CONC_MASC",
                "titulo": "Sexo Masculino - Matriculados x Concluintes",
                "cor_mat": "#3366cc",   # Azul forte
                "cor_conc": "#66ccff"   # Azul claro
            },
            "Feminino": {
                "mat": "QT_MAT_FEM",
                "conc": "QT_CONC_FEM",
                "titulo": "Sexo Feminino - Matriculados x Concluintes",
                "cor_mat": "#e377c2",   # Rosa
                "cor_conc": "#ff7f0e"   # Laranja
            }
        }

        # Calcula o maior valor do eixo y para padronizar
        colunas_analise = [
            "QT_MAT", "QT_CONC",
            "QT_MAT_MASC", "QT_CONC_MASC",
            "QT_MAT_FEM", "QT_CONC_FEM"
        ]
        dados_ano = dados.groupby("NU_ANO_CENSO")[colunas_analise].sum()
        maior_valor_y = dados_ano.max().max()

        escolha = st.radio("Escolha o recorte:", list(opcoes.keys()), horizontal=True)
        grupo = opcoes[escolha]
        dados_filtrados = dados.groupby('NU_ANO_CENSO')[[grupo["mat"], grupo["conc"]]].sum()

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=dados_filtrados.index,
            y=dados_filtrados[grupo["mat"]],
            name="Matriculados",
            marker_color=grupo["cor_mat"]
        ))
        fig.add_trace(go.Bar(
            x=dados_filtrados.index,
            y=dados_filtrados[grupo["conc"]],
            name="Concluintes",
            marker_color=grupo["cor_conc"]
        ))

        fig.update_layout(
            title=grupo["titulo"],
            barmode="group",
            yaxis_range=[0, maior_valor_y * 1.1]
        )

        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(dados_filtrados, use_container_width=True)
    #---------------------------------------------------------------------    
    with st.expander("🔹2. Existe diferença de evasão entre cursos noturnos e diurnos?"):
        st.subheader("🔹2. Existe diferença de evasão entre cursos noturnos e diurnos?")


        anos_disponiveis = sorted(dados["NU_ANO_CENSO"].unique())

        # --- Botão para selecionar tipo de visualização ---
        opcao = st.radio("Escolha a análise:", ["Geral", "Ao longo do tempo"], horizontal=True)

        if opcao == "Geral":
            # Somatório de todos os anos
            total_geral = {
                "Turno": ["Diurno", "Diurno", "Noturno", "Noturno"],
                "Tipo": ["Matriculados", "Concluintes", "Matriculados", "Concluintes"],
                "Total": [
                    dados["QT_MAT_DIURNO"].sum(),
                    dados["QT_CONC_DIURNO"].sum(),
                    dados["QT_MAT_NOTURNO"].sum(),
                    dados["QT_CONC_NOTURNO"].sum(),
                ]
            }
            df_geral = pd.DataFrame(total_geral)

            fig_geral = px.bar(df_geral, x="Turno", y="Total", color="Tipo", barmode="group", text_auto=True,
                            color_discrete_map={"Matriculados": "#1f77b4", "Concluintes": "#2ca02c"})
            fig_geral.update_layout(title="Total Geral - Matriculados vs Concluintes por Turno", yaxis_title="Total de Alunos")
            st.plotly_chart(fig_geral)

        else:
            col1, col2 = st.columns(2)

            # Diurno ao longo do tempo
            with col1:
                dados_diurno = dados.groupby("NU_ANO_CENSO")[["QT_MAT_DIURNO", "QT_CONC_DIURNO"]].sum()
                fig_diurno = go.Figure()
                fig_diurno.add_trace(go.Bar(x=dados_diurno.index, y=dados_diurno["QT_MAT_DIURNO"],
                                            name="Matriculados", marker_color="#1f77b4"))
                fig_diurno.add_trace(go.Bar(x=dados_diurno.index, y=dados_diurno["QT_CONC_DIURNO"],
                                            name="Concluintes", marker_color="#2ca02c"))
                fig_diurno.update_layout(
                    title="Diurno - Ao longo do tempo",
                    barmode="group",
                    yaxis_title="Alunos",
                    xaxis=dict(tickmode='array', tickvals=anos_disponiveis, ticktext=[str(ano) for ano in anos_disponiveis])
                )
                st.plotly_chart(fig_diurno)

            # Noturno ao longo do tempo
            with col2:
                dados_noturno = dados.groupby("NU_ANO_CENSO")[["QT_MAT_NOTURNO", "QT_CONC_NOTURNO"]].sum()
                fig_noturno = go.Figure()
                fig_noturno.add_trace(go.Bar(x=dados_noturno.index, y=dados_noturno["QT_MAT_NOTURNO"],
                                            name="Matriculados", marker_color="#1f77b4"))
                fig_noturno.add_trace(go.Bar(x=dados_noturno.index, y=dados_noturno["QT_CONC_NOTURNO"],
                                            name="Concluintes", marker_color="#2ca02c"))
                fig_noturno.update_layout(
                    title="Noturno - Ao longo do tempo",
                    barmode="group",
                    yaxis_title="Alunos",
                    xaxis=dict(tickmode='array', tickvals=anos_disponiveis, ticktext=[str(ano) for ano in anos_disponiveis])
                )
                st.plotly_chart(fig_noturno)
    #--------------------------------------------------------------------
    with st.expander("🔹3. A evasão varia entre faixas etárias?"):
        st.subheader("🔹3. A evasão varia entre faixas etárias?")

                # === DADOS ===
        faixa_etaria_mat = ['QT_MAT_0_17', 'QT_MAT_18_24','QT_MAT_25_29', 'QT_MAT_30_34', 'QT_MAT_35_39', 'QT_MAT_40_49','QT_MAT_50_59', 'QT_MAT_60_MAIS']
        faixa_etaria_conc = ['QT_CONC_0_17', 'QT_CONC_18_24', 'QT_CONC_25_29','QT_CONC_30_34', 'QT_CONC_35_39', 'QT_CONC_40_49', 'QT_CONC_50_59','QT_CONC_60_MAIS']
        faixa_etaria_padronizada = ['0-17', '18-24', '25-29', '30-34', '35-39', '40-49', '50-59', '60+']

        # === SOMA GERAL DE FAIXA ETÁRIA ===
        valores_mat = dados[faixa_etaria_mat].sum()
        valores_conc = dados[faixa_etaria_conc].sum()

        # === ABA DE NAVEGAÇÃO ===
        aba = st.radio("Selecione a visualização", ["📊 Gráfico Geral", "🎓 Curso por Faixa Etária", "📋 Tabela de Porcentagens"])

        # === 1. GRÁFICO GERAL ===
        if aba == "📊 Gráfico Geral":
            fig = go.Figure()
            fig.add_trace(go.Bar(x=faixa_etaria_padronizada, y=valores_mat, name="Matriculados", marker_color="#636EFA"))
            fig.add_trace(go.Bar(x=faixa_etaria_padronizada, y=valores_conc, name="Concluintes", marker_color="#EF553B"))
            fig.update_layout(
                title="Matriculados x Concluintes por Faixa Etária (Geral)",
                xaxis_title="Faixa Etária",
                yaxis_title="Quantidade",
                barmode="group"
            )
            st.plotly_chart(fig)

        # === 2. RELAÇÃO CURSO X FAIXA ETÁRIA ===
        elif aba == "🎓 Curso por Faixa Etária":
            curso_selecionado = st.selectbox("Selecione um curso (NO_CINE_AREA_GERAL)", sorted(dados["NO_CINE_AREA_GERAL"].unique()))
            dados_filtrados = dados[dados["NO_CINE_AREA_GERAL"] == curso_selecionado]
            
            mat_curso = dados_filtrados[faixa_etaria_mat].sum()
            conc_curso = dados_filtrados[faixa_etaria_conc].sum()
            
            fig = go.Figure()
            fig.add_trace(go.Bar(x=faixa_etaria_padronizada, y=mat_curso, name="Matriculados", marker_color="#00CC96"))
            fig.add_trace(go.Bar(x=faixa_etaria_padronizada, y=conc_curso, name="Concluintes", marker_color="#AB63FA"))
            fig.update_layout(
                title=f"Matriculados x Concluintes por Faixa Etária - Curso: {curso_selecionado}",
                xaxis_title="Faixa Etária",
                yaxis_title="Quantidade",
                barmode="group"
            )
            st.plotly_chart(fig)

        # === 3. TABELA DE PORCENTAGENS ===
        elif aba == "📋 Tabela de Porcentagens":
           # --- TABELA DE PORCENTAGENS ---
                soma_mat_total = valores_mat.sum()
                soma_conc_total = valores_conc.sum()

                # Garante que as porcentagens tenham mesmo tamanho que as faixas
                porcent_mat = (valores_mat / soma_mat_total * 100).round(2).tolist()
                porcent_conc = (valores_conc / soma_conc_total * 100).round(2).tolist()

                df_percentual = pd.DataFrame({
                    'Faixa Etária': faixa_etaria_padronizada,
                    '% Matriculados': porcent_mat,
                    '% Concluintes': porcent_conc
                })

                st.subheader("Percentual por Faixa Etária")
                st.dataframe(df_percentual, use_container_width=True)

    #--------------------------------------------------------------------
    with st.expander("🔹4. A cor/raça influencia na taxa de evasão?"):
        st.subheader("🔹4. A cor/raça influencia na taxa de evasão?")

        # 🔹 Dados agrupados por ano
        dados_agrupados = dados.groupby("NU_ANO_CENSO").sum()

        # 🔹 Definição das variáveis
        cor_raca_mat = ['QT_MAT_BRANCA', 'QT_MAT_PRETA', 'QT_MAT_PARDA', 'QT_MAT_AMARELA', 'QT_MAT_INDIGENA', 'QT_MAT_CORND']
        cor_raca_conc = ['QT_CONC_BRANCA', 'QT_CONC_PRETA', 'QT_CONC_PARDA', 'QT_CONC_AMARELA', 'QT_CONC_INDIGENA', 'QT_CONC_CORND']
        cor_raca_padronizada = ['Branca', 'Preta', 'Parda', 'Amarela', 'Indígena', 'Cor Não Declarada']

        # 🔹 Opções para escolha da aba
        aba = st.radio("Escolha a análise:", ["📈 Evolução por Raça", "📊 Comparação entre Raças", "👨‍👩‍👧‍👦 Comparação por Gênero"])

        # 🔹 1. Evolução por raça (Gráfico de linhas)
        if aba == "📈 Evolução por Raça":
            raca_selecionada = st.selectbox("Selecione uma raça:", cor_raca_padronizada)
            index_raca = cor_raca_padronizada.index(raca_selecionada)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=dados_agrupados.index, y=dados_agrupados[cor_raca_mat[index_raca]],
                mode="lines+markers", name="Matriculados", line=dict(color="blue")
            ))
            fig.add_trace(go.Scatter(
                x=dados_agrupados.index, y=dados_agrupados[cor_raca_conc[index_raca]],
                mode="lines+markers", name="Concluintes", line=dict(color="green")
            ))

            fig.update_layout(
                title=f"Evolução de Matriculados e Concluintes - {raca_selecionada}",
                xaxis_title="Ano", yaxis_title="Quantidade", template="plotly_white"
            )
            st.plotly_chart(fig)

        # 🔹 2. Comparação entre Raças (Gráfico de barras)
        elif aba == "📊 Comparação entre Raças":
            valores_mat = dados[cor_raca_mat].sum().values
            valores_conc = dados[cor_raca_conc].sum().values

            fig = go.Figure()
            fig.add_trace(go.Bar(x=cor_raca_padronizada, y=valores_mat, name="Matriculados", marker_color="royalblue"))
            fig.add_trace(go.Bar(x=cor_raca_padronizada, y=valores_conc, name="Concluintes", marker_color="seagreen"))

            fig.update_layout(
                title="Comparação de Matrículas e Conclusões por Raça",
                xaxis_title="Raça", yaxis_title="Quantidade", barmode="group", template="plotly_white"
            )
            st.plotly_chart(fig)

        # 🔹 3. Comparação por Gênero (Gráfico de barras)
        elif aba == "👨‍👩‍👧‍👦 Comparação por Gênero":
                    # 🔹 Somando os valores de matrícula e conclusão por gênero e raça
            valores_masc_mat = dados.groupby("NU_ANO_CENSO")["QT_MAT_MASC"].sum()
            valores_masc_conc = dados.groupby("NU_ANO_CENSO")["QT_CONC_MASC"].sum()
            valores_fem_mat = dados.groupby("NU_ANO_CENSO")["QT_MAT_FEM"].sum()
            valores_fem_conc = dados.groupby("NU_ANO_CENSO")["QT_CONC_FEM"].sum()

            # 🔹 Criando gráfico de barras com todas as raças juntas
            fig = go.Figure()
            fig.add_trace(go.Bar(x=cor_raca_padronizada, y=valores_masc_mat, name="Matriculados - Homens", marker_color="blue"))
            fig.add_trace(go.Bar(x=cor_raca_padronizada, y=valores_masc_conc, name="Concluintes - Homens", marker_color="lightblue"))
            fig.add_trace(go.Bar(x=cor_raca_padronizada, y=valores_fem_mat, name="Matriculados - Mulheres", marker_color="purple"))
            fig.add_trace(go.Bar(x=cor_raca_padronizada, y=valores_fem_conc, name="Concluintes - Mulheres", marker_color="pink"))

            fig.update_layout(
                title="Matrículas e Conclusões por Raça e Gênero",
                xaxis_title="Raça",
                yaxis_title="Quantidade",
                barmode="group",
                template="plotly_white"
            )

            st.plotly_chart(fig)

  #--------------------------------------------------------------------
    with st.expander("🔹5. Alunos com deficiência têm maior evasão?"):
        st.subheader("🔹5. Alunos com deficiência têm maior evasão?")

        # 🔹 Opções de visualização
        aba = st.radio("Escolha a análise:", ["📊 Total Geral", "🏫 Comparação por Universidade", "🏢 Comparação por Rede"])

        # 🔹 1. Total de Matriculados e Concluintes
        if aba == "📊 Total Geral":
            matriculados_total = dados["QT_MAT_DEFICIENTE"].sum()
            concluintes_total = dados["QT_CONC_DEFICIENTE"].sum()

            fig = go.Figure()
            fig.add_trace(go.Bar(x=["Matriculados", "Concluintes"], y=[matriculados_total, concluintes_total], marker_color=["blue", "green"]))

            fig.update_layout(
                title="Total de Matriculados e Concluintes - Pessoas com Deficiência",
                xaxis_title="Status",
                yaxis_title="Quantidade",
                template="plotly_white"
            )

            st.plotly_chart(fig)

        # 🔹 2. Comparação por Universidade (`SG_IES`)
        elif aba == "🏫 Comparação por Universidade":
            dados_universidades = dados.groupby("SG_IES")[["QT_MAT_DEFICIENTE", "QT_CONC_DEFICIENTE"]].sum()

            fig = go.Figure()
            fig.add_trace(go.Bar(x=dados_universidades.index, y=dados_universidades["QT_MAT_DEFICIENTE"], name="Matriculados", marker_color="blue"))
            fig.add_trace(go.Bar(x=dados_universidades.index, y=dados_universidades["QT_CONC_DEFICIENTE"], name="Concluintes", marker_color="green"))

            fig.update_layout(
                title="Matrículas e Conclusões por Universidade - Pessoas com Deficiência",
                xaxis_title="Universidade",
                yaxis_title="Quantidade",
                barmode="group",
                template="plotly_white"
            )

            st.plotly_chart(fig)

        # 🔹 3. Comparação por Rede (`TP_REDE`)
        elif aba == "🏢 Comparação por Rede":
            dados_redes = dados.groupby("TP_REDE")[["QT_MAT_DEFICIENTE", "QT_CONC_DEFICIENTE"]].sum()

            fig = go.Figure()
            fig.add_trace(go.Bar(x=dados_redes.index, y=dados_redes["QT_MAT_DEFICIENTE"], name="Matriculados", marker_color="blue"))
            fig.add_trace(go.Bar(x=dados_redes.index, y=dados_redes["QT_CONC_DEFICIENTE"], name="Concluintes", marker_color="green"))

            fig.update_layout(
                title="Matrículas e Conclusões por Rede de Ensino - Pessoas com Deficiência",
                xaxis_title="Rede de Ensino",
                yaxis_title="Quantidade",
                barmode="group",
                template="plotly_white"
            )

            st.plotly_chart(fig)
     