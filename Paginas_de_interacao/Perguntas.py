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

        tab1, tab2, tab3 = st.tabs(["Geral", "Masculino", "Feminino"])

        with tab1:
            st.subheader("🔹 Explicação - Geral")
        
            texto = """
            A análise dos dados revela uma tendência interessante sobre a evolução do número de alunos matriculados e concluintes ao longo dos anos. De 2018 a 2023, houve um crescimento no número de matriculados, saindo de 85.920 em 2018 para 94.868 em 2023. Por outro lado, o número de concluintes flutuou, começando em 16.031 em 2018, caindo até 12.372 em 2021 e voltando a subir para 14.718 em 2023.

            Essa discrepância entre o aumento dos matriculados e a variação dos concluintes pode indicar desafios no percurso acadêmico dos alunos, como dificuldades em concluir o curso dentro do período esperado. O crescimento contínuo de matrículas sugere uma demanda crescente pela educação ao longo dos anos, o que pode estar relacionado a fatores como expansão da oferta educacional, aumento da acessibilidade ou mudanças na percepção da importância dos estudos.
            """
            st.write(texto)

        with tab2:
            st.subheader("🔹 Explicação - Masculino")
            st.write("""
            A análise dos dados evidencia uma diferença significativa entre o número de homens matriculados e homens concluintes nos cursos de graduação ao longo dos anos. Entre 2018 e 2023, a quantidade de matriculados manteve-se relativamente estável, com pequenos aumentos anuais, enquanto o número de concluintes variou, apresentando uma queda acentuada em 2020 e 2021, seguida por um leve crescimento até 2023.
            Esse comportamento sugere possíveis dificuldades enfrentadas pelos alunos no decorrer do curso, como evasão, trancamento de matrícula ou dificuldades acadêmicas, impedindo a conclusão dentro do período esperado. Além disso, a quantidade relativamente baixa de concluintes em comparação aos matriculados pode indicar desafios estruturais na retenção dos estudantes, demandando investigações mais aprofundadas sobre os fatores que afetam essa trajetória acadêmica.
            📊 A evolução dos dados sugere que, embora haja um crescimento contínuo no número de ingressantes, a conclusão do curso ainda representa um desafio para muitos alunos, o que pode estar ligado a fatores como condições financeiras, qualidade da oferta educacional, suporte acadêmico e motivação ao longo dos anos.
            Se quiser, posso te ajudar a explorar hipóteses específicas sobre essa tendência! 😃
            """)

        with tab3:
            st.subheader("🔹 Explicação - Feminino")
            st.write("""
            O gráfico apresenta a relação entre homens matriculados e homens concluintes no ensino superior ao longo dos anos 2018 a 2023. Observa-se que, embora o número de matriculados tenha tido variações pequenas entre os anos, o número de concluintes é significativamente menor, evidenciando uma possível taxa de evasão expressiva.
                     
            Em 2018, havia aproximadamente 38.447 homens matriculados, enquanto apenas 6.741 concluíram seus cursos. Essa diferença se mantém nos anos seguintes, com o menor número de conclusões em 2021 (5.146 concluíram), o que pode sugerir dificuldades enfrentadas pelos alunos naquele período.
                     
            Por outro lado, em 2023, há um leve aumento no número de concluintes (6.021), o que pode indicar uma melhora na retenção estudantil ou adaptações institucionais para incentivar a finalização dos cursos.
            Esses dados podem ser utilizados para investigar fatores que influenciam a evasão, como políticas educacionais, dificuldades financeiras, estrutura curricular e suporte acadêmico.
            Se quiser, posso te ajudar a aprofundar ainda mais essa análise! 🚀
            """)

       


   


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

        tab1, tab2= st.tabs(["Geral", "Ao longo do Tempo"])
        
        with tab1:
            st.subheader("🔹 Explicação - Geral")
            st.write("""
            A análise dos dados revela um contraste significativo entre a evasão nos cursos diurnos e noturnos. Os números indicam que os cursos diurnos possuem um maior volume de matriculados, com 329.370 alunos, enquanto os cursos noturnos registram 165.148 matrículas.
            Entretanto, ao analisar os concluintes, nota-se uma diferença substancial na retenção acadêmica. Nos cursos diurnos, 49.381 alunos concluíram seus estudos, enquanto nos noturnos, apenas 28.097 alunos finalizaram seus cursos. Essa discrepância pode sugerir desafios específicos para estudantes do turno noturno, como conciliar trabalho e estudo, maior carga horária diária e dificuldades de acesso a recursos acadêmicos.
            O crescimento da matrícula ao longo dos anos demonstra uma demanda contínua pelo ensino superior, mas a disparidade na conclusão evidencia barreiras que podem impactar diretamente a trajetória acadêmica dos alunos. Investigar os fatores que influenciam essa diferença pode fornecer insights estratégicos para reduzir a evasão e melhorar a retenção estudantil nos cursos noturnos.
            Se quiser, posso aprofundar essa análise com hipóteses adicionais! 🚀

            """)


        with tab2:
            st.subheader("🔹 Explicação - Ao longo do Tempo")
            st.write("""
            A análise dos dados revela um padrão interessante na matrícula e conclusão de homens no ensino superior ao longo dos anos 2018 a 2023. Durante esse período, o número de matriculados manteve-se relativamente estável, oscilando entre 38.447 e 42.011 alunos, enquanto o número de concluintes apresentou flutuações mais acentuadas.
            Observa-se que em 2021, houve o menor número de homens concluintes, com 5.146 alunos, o que pode sugerir dificuldades enfrentadas por estudantes naquele período. Já em 2023, houve um leve crescimento no total de concluintes, alcançando 6.021 alunos.
            A discrepância entre matriculados e concluintes pode indicar barreiras no percurso acadêmico, como dificuldades financeiras, carga horária intensa ou desafios institucionais que impactam a permanência dos alunos até a finalização do curso. Essa tendência reforça a necessidade de medidas para reduzir a evasão e melhorar o suporte acadêmico, garantindo que mais alunos possam concluir seus estudos dentro do tempo esperado. 🚀📊
            Se precisar de uma análise mais aprofundada, posso explorar hipóteses adicionais!
            """)

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

        tab1, tab2,tab3= st.tabs(["Geral", "Por faixa Etária","Tabela Porcentagem"])
        
        with tab1:
            st.subheader("🔹 Explicação - Geral")
            st.write("""
            A análise dos dados evidencia a relação entre a evasão e a faixa etária dos estudantes do ensino superior. Ao longo dos anos, percebe-se que a maioria dos matriculados pertence à faixa de 18-24 anos, com mais de 350.000 alunos, enquanto o número de concluintes nessa faixa etária é significativamente menor.
            Ao observar os padrões de evasão, notamos que os alunos mais jovens apresentam uma taxa de conclusão inferior à esperada. Isso pode estar relacionado a desafios como adaptação acadêmica, mudanças na vida pessoal ou dificuldades financeiras que afetam sua permanência no curso. Já nas faixas etárias acima de 30 anos, os números de matrícula diminuem, mas ainda há uma diferença relevante entre ingressantes e concluintes, sugerindo que a permanência no ensino superior também pode ser desafiadora para adultos em formação.
            O crescimento da matrícula reflete um interesse contínuo pela educação superior, mas a diferença no número de concluintes destaca a necessidade de estratégias para aumentar a retenção, oferecendo suporte acadêmico adequado e políticas para reduzir a evasão. 🚀📊
            Se quiser aprofundar essa investigação, posso te ajudar a explorar hipóteses adicionais!


            """)
        with tab2:
            st.subheader("🔹 Explicação - Por faixa Etária")
            st.write("""
            A análise dos dados evidencia como a evasão no ensino superior varia entre diferentes faixas etárias. O gráfico apresenta informações sobre matrículas e conclusões no curso "Agricultura, Silvicultura, Pesca e Veterinária", comparando a trajetória acadêmica dos estudantes conforme sua idade.
            Observa-se que a maioria dos matriculados pertence à faixa 18-24 anos, indicando que essa é a idade predominante para ingresso no curso. No entanto, há uma redução significativa no número de concluintes dentro dessa mesma faixa etária, sugerindo que muitos alunos enfrentam dificuldades para concluir a graduação.
            Para faixas etárias mais avançadas, como 30 anos ou mais, o número de matriculados é menor, mas a evasão continua evidente, pois a quantidade de concluintes também é reduzida. Esse padrão pode estar associado a fatores como conciliar trabalho e estudos, carga horária exigente, desafios financeiros ou mudanças na vida pessoal que impactam a continuidade do curso.
            A análise reforça a importância de políticas educacionais voltadas para a retenção de alunos, garantindo suporte acadêmico adequado para reduzir a evasão e melhorar as taxas de conclusão. 🚀📊
            Se quiser, posso te ajudar a explorar hipóteses adicionais sobre essa relação!
            """)
        with tab3:    
            st.subheader("🔹 Explicação - Tabela Porcentagem")
            st.write("""
            A análise dos dados revela uma relação entre a evasão no ensino superior e a faixa etária dos estudantes matriculados no curso de Agricultura, Silvicultura, Pesca e Veterinária. Como esperado, a maioria dos matriculados pertence à faixa 18-24 anos, indicando que essa é a idade predominante para ingresso na graduação. No entanto, observa-se uma significativa redução no número de concluintes dentro dessa mesma faixa etária.
            Nas faixas 25-29 anos e 30-34 anos, o número de matriculados é menor, mas ainda há uma diferença expressiva entre ingressantes e concluintes, sugerindo desafios na conclusão dos cursos. Já em faixas etárias acima de 40 anos, tanto as matrículas quanto as conclusões são mais reduzidas, o que pode indicar menor adesão ao ensino superior nessa fase da vida.
            Esses padrões podem estar relacionados a fatores como dificuldades acadêmicas, necessidade de conciliar trabalho e estudos, questões financeiras ou mudanças na vida pessoal. A identificação dessas barreiras é fundamental para desenvolver estratégias voltadas à retenção estudantil, garantindo que mais alunos consigam concluir seus cursos e reduzir as taxas de evasão. 🚀📊
            Se quiser aprofundar essa análise, posso explorar hipóteses adicionais sobre essa 

            """)

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

        tab1, tab2,tab3= st.tabs(["Evolução por Raça", "Comparação raça","Comparação Gênero"])
        
        with tab1:
            st.subheader("🔹 Explicação - Evolução por Raça")
            st.write("""
            A análise dos dados revela o impacto da cor/raça na taxa de evasão no ensino superior. O gráfico mostra a evolução do número de matriculados e concluintes na categoria Branca entre os anos 2018 e 2023.
            Os dados indicam que, ao longo dos anos, houve uma leve queda no número de matriculados entre 2018 e 2021, seguido por um pequeno aumento até 2023. Já a quantidade de concluintes apresenta um padrão semelhante, com redução até 2021 e crescimento discreto nos últimos anos.
            Essa diferença entre matriculados e concluintes pode sugerir que determinados fatores, como acesso à educação, suporte acadêmico, desafios financeiros e políticas institucionais, influenciam a permanência dos alunos no curso. A análise pode ser expandida para identificar se há diferenças significativas entre grupos raciais, contribuindo para um entendimento mais profundo sobre desigualdades na evasão universitária.
            Se quiser explorar comparações entre diferentes raças ou gêneros, posso ajudar a estruturar essa análise! 🚀



            """)
        with tab2:
            st.subheader("🔹 Explicação - Comparação raça")
            st.write("""
            A análise dos dados revela a evolução do número de matriculados e concluintes na categoria racial Branca entre os anos 2018 e 2023. O gráfico mostra que, ao longo dos anos, houve uma leve queda no total de matriculados, passando de cerca de 35.000 em 2018 para 30.000 em 2023. Já a quantidade de concluintes também diminuiu, indo de 5.000 em 2018 para aproximadamente 3.000 em 2023.
            Essa discrepância entre o número de alunos que ingressam e aqueles que concluem seus cursos pode indicar fatores que impactam a permanência acadêmica, como dificuldades financeiras, adaptação ao ensino superior ou até mesmo acesso a suporte educacional adequado. O padrão observado sugere que a taxa de conclusão não acompanha o número de ingressantes ao longo dos anos, o que pode representar um desafio para a redução da evasão estudantil

            """)
        with tab3:    
            st.subheader("🔹 Explicação - Comparação Gênero")
            st.write("""
            A análise dos dados revela uma relação entre a evasão no ensino superior e fatores como raça e gênero. O gráfico apresenta a comparação entre matriculados e concluintes em diferentes grupos raciais, subdivididos por gênero.
            📊 Principais tendências observadas:
            - Em todos os grupos raciais, o número de matriculados é significativamente maior do que o de concluintes, evidenciando uma taxa de evasão expressiva.
            - Tanto homens quanto mulheres apresentam padrões semelhantes, com altos índices de matrícula, mas uma conclusão consideravelmente inferior.
            - A categoria "Cor Não Declarada" tem uma baixa representatividade, sugerindo que parte dos estudantes opta por não informar sua raça ao ingressar no ensino superior.
            Essa discrepância entre ingresso e conclusão pode indicar barreiras acadêmicas, sociais ou econômicas, que impactam diferentes grupos de forma distinta. Investigar essas diferenças pode contribuir para estratégias de retenção estudantil e promoção de políticas mais inclusivas para a permanência dos alunos no ensino superior. 🚀📊
            Se quiser explorar comparações mais detalhadas ou hipóteses adicionais, posso te ajudar com essa análise!
            """)

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
    #--------------------------------------------------------------------
    with st.expander("🔹6. A evasão é diferente entre cursos de áreas diferentes?"):
        st.subheader("🔹6. A evasão é diferente entre cursos de áreas diferentes?")

        
        # 🔹 Escolha de visualização
        aba = st.radio("Selecione a análise:", [
            "📊 Matrículas e Concluintes por Categoria",
            "📌 Comparação por Categoria Específica",
            "🔍 Análise Detalhada por Área"
        ])

        # 🔹 1. Gráfico de Barras por `NO_CINE_AREA_GERAL`
        if aba == "📊 Matrículas e Concluintes por Categoria":
            dados_geral = dados.groupby("NO_CINE_AREA_GERAL")[["QT_MAT", "QT_CONC"]].sum()

            fig = go.Figure()
            fig.add_trace(go.Bar(y=dados_geral.index, x=dados_geral["QT_MAT"], name="Matriculados", marker_color="blue", orientation='h'))
            fig.add_trace(go.Bar(y=dados_geral.index, x=dados_geral["QT_CONC"], name="Concluintes", marker_color="green", orientation='h'))

            fig.update_layout(
                title="Matrículas e Concluintes por Categoria",
                xaxis_title="Quantidade",
                yaxis_title="Categoria",
                barmode="group",
                template="plotly_white"
            )

            st.plotly_chart(fig)

        # 🔹 2. Comparação por `NO_CINE_AREA_ESPECIFICA`
        elif aba == "📌 Comparação por Categoria Específica":
            categoria_especifica = st.selectbox("Selecione uma categoria específica:", sorted(dados["NO_CINE_AREA_ESPECIFICA"].unique()))
            
            dados_filtrados = dados[dados["NO_CINE_AREA_ESPECIFICA"] == categoria_especifica]
            dados_especificos = dados_filtrados.groupby("NO_CINE_AREA_DETALHADA")[["QT_MAT", "QT_CONC"]].sum()

            fig = go.Figure()
            fig.add_trace(go.Bar(y=dados_especificos.index, x=dados_especificos["QT_MAT"], name="Matriculados", marker_color="blue", orientation='h'))
            fig.add_trace(go.Bar(y=dados_especificos.index, x=dados_especificos["QT_CONC"], name="Concluintes", marker_color="green", orientation='h'))

            fig.update_layout(
                title=f"Comparação em {categoria_especifica}",
                xaxis_title="Quantidade",
                yaxis_title="Área Detalhada",
                barmode="group",
                template="plotly_white"
            )

            st.plotly_chart(fig)

        # 🔹 3. Análise Detalhada por `NO_CINE_AREA_DETALHADA`
        elif aba == "🔍 Análise Detalhada por Área":
            categoria_especifica = st.selectbox("Selecione uma categoria específica:", sorted(dados["NO_CINE_AREA_ESPECIFICA"].unique()))
            dados_filtrados = dados[dados["NO_CINE_AREA_ESPECIFICA"] == categoria_especifica]

            # 🔹 Criando tabela de análise por área detalhada
            dados_detalhados = dados_filtrados.groupby("NO_CINE_AREA_DETALHADA").agg({
                "QT_MAT": "sum",
                "QT_CONC": "sum",
                "QT_MAT_MASC": "sum",
                "QT_CONC_MASC": "sum",
                "QT_MAT_FEM": "sum",
                "QT_CONC_FEM": "sum"
            }).reset_index()

            # 🔹 Determinando raça predominante por área
            dados_filtrados["Raça Predominante"] = dados_filtrados[
                ["QT_MAT_BRANCA", "QT_MAT_PRETA", "QT_MAT_PARDA", "QT_MAT_AMARELA", "QT_MAT_INDIGENA"]
            ].idxmax(axis=1)
            
            dados_raca = dados_filtrados.groupby("NO_CINE_AREA_DETALHADA")["Raça Predominante"].first().reset_index()

            # 🔹 Unindo os dados detalhados com a predominância racial
            df_final = pd.merge(dados_detalhados, dados_raca, on="NO_CINE_AREA_DETALHADA")

            # 🔹 Exibindo a tabela
            st.subheader(f"Análise Detalhada por Área - {categoria_especifica}")
            st.dataframe(df_final, use_container_width=True)

    #--------------------------------------------------------------------
    with st.expander("🔹7. A evasão é maior em cursos EAD?"):
        st.subheader("🔹7. A evasão é maior em cursos EAD?")

                # 🔹 Escolha de visualização
        aba = st.radio("Selecione a análise:", [
            "📊 Total de Matriculados e Concluintes",
            "🏫 Comparação entre Modalidade de Ensino e Rede",
            "🏢 Comparação entre Modalidade de Ensino e Universidade"
        ])

        # 🔹 1. Total Geral de Matriculados e Concluintes
        if aba == "📊 Total de Matriculados e Concluintes":
            total_matriculados = dados["QT_MAT"].sum()
            total_concluintes = dados["QT_CONC"].sum()

            fig = go.Figure()
            fig.add_trace(go.Bar(x=["Matriculados"], y=[total_matriculados], name="Matriculados"))
            fig.add_trace(go.Bar(x=["Concluintes"], y=[total_concluintes], name="Concluintes"))

            fig.update_layout(
                title="Total de Matriculados e Concluintes",
                xaxis_title="Status",
                yaxis_title="Quantidade",
                template="plotly_white"
            )

            st.plotly_chart(fig)

        # 🔹 2. Comparação entre `TP_MODALIDADE_ENSINO` e `TP_REDE`
        elif aba == "🏫 Comparação entre Modalidade de Ensino e Rede":
            dados_modalidade_rede = dados.groupby(["TP_MODALIDADE_ENSINO", "TP_REDE"])[["QT_MAT", "QT_CONC"]].sum().reset_index()

            fig = go.Figure()
            for _, row in dados_modalidade_rede.iterrows():
                modalidade = "Presencial" if row["TP_MODALIDADE_ENSINO"] == 1 else "A Distância"
                rede = row["TP_REDE"]

                fig.add_trace(go.Bar(x=[modalidade], y=[row["QT_MAT"]], name=f"Matriculados - Rede {rede}"))
                fig.add_trace(go.Bar(x=[modalidade], y=[row["QT_CONC"]], name=f"Concluintes - Rede {rede}"))

            fig.update_layout(
                title="Comparação entre Modalidade de Ensino e Rede",
                xaxis_title="Modalidade de Ensino",
                yaxis_title="Quantidade",
                barmode="group",
                template="plotly_white"
            )

            st.plotly_chart(fig)

        # 🔹 3. Comparação entre `TP_MODALIDADE_ENSINO` e `SG_IES`
        elif aba == "🏢 Comparação entre Modalidade de Ensino e Universidade":
            dados_modalidade_universidade = dados.groupby(["TP_MODALIDADE_ENSINO", "SG_IES"])[["QT_MAT", "QT_CONC"]].sum().reset_index()

            fig = go.Figure()
            for _, row in dados_modalidade_universidade.iterrows():
                modalidade = "Presencial" if row["TP_MODALIDADE_ENSINO"] == 1 else "A Distância"
                universidade = row["SG_IES"]

                fig.add_trace(go.Bar(x=[modalidade], y=[row["QT_MAT"]], name=f"Matriculados - {universidade}"))
                fig.add_trace(go.Bar(x=[modalidade], y=[row["QT_CONC"]], name=f"Concluintes - {universidade}"))

            fig.update_layout(
                title="Comparação entre Modalidade de Ensino e Universidade",
                xaxis_title="Modalidade de Ensino",
                yaxis_title="Quantidade",
                barmode="group",
                template="plotly_white"
            )

            st.plotly_chart(fig)

    #--------------------------------------------------------------------
    with st.expander("🔹 8. Qual é a distribuição racial dos estudantes em cada área do ensino superior?"):
            st.subheader("🔹 8. Distribuição racial dos estudantes por área do ensino superior")

            # 🔹 Agrupa por área geral e soma por cor/raça
            agrupado = dados.groupby('NO_CINE_AREA_GERAL')[[
                'QT_MAT_BRANCA', 'QT_MAT_PRETA', 'QT_MAT_PARDA', 'QT_MAT_AMARELA', 'QT_MAT_INDIGENA'
            ]].sum()

            # 🔹 Calcula proporção por linha
            proporcoes = agrupado.div(agrupado.sum(axis=1), axis=0).reset_index()

            # 🔹 Criando mapa de calor interativo com os valores corretos
            fig = px.imshow(
                proporcoes.iloc[:, 1:].values,  # 🔹 Passando apenas os valores da matriz
                x=proporcoes.columns[1:],  # 🔹 Definindo corretamente os rótulos do eixo X
                y=proporcoes["NO_CINE_AREA_GERAL"],  # 🔹 Definindo corretamente os rótulos do eixo Y
                color_continuous_scale="YlGnBu",
                labels={"x": "Cor/Raça", "y": "Área Geral do Conhecimento", "color": "Proporção"},
            )

                    # 🔹 Melhorando interatividade
            fig.update_layout(
            title="Mapa de Calor Interativo - Proporção de Matrículas por Cor/Raça",
            xaxis_title="Cor/Raça",
            yaxis_title="Área Geral do Conhecimento",
            template="plotly_white",
            width=100,  # 🔹 Ajusta a largura do gráfico
            height=900   # 🔹 Ajusta a altura do gráfico
        )


            # 🔹 Exibir gráfico corretamente no Streamlit
            st.plotly_chart(fig)




