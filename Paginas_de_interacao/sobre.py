import streamlit as st

def exibir():
  st.title("📁 Sobre os Dados")
  tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
      "📊 Tratamento dos Dados", 
      "🗂 Base de Dados Utilizada", 
      "🏫 Instituições Selecionadas",
      "🔍 Dados Faltantes e Duplicados",
      "📌 Ajustes e Transformações",
      "🛠️ Normalização dos Dados",
      "🔍 Análise Crítica"
  ])

  # ----------------------------------------------------------------------------
  # 📊 Tratamento dos Dados
  # ----------------------------------------------------------------------------
  with tab1:
      st.header("Tratamento e Recorte dos Dados")

      st.write("""
      Neste estudo, os dados do **Censo da Educação Superior** foram tratados com foco exclusivo no **Distrito Federal (DF)**.  
      A escolha desse recorte geográfico busca reduzir o volume de dados e aumentar a profundidade da análise, permitindo uma investigação mais detalhada.
      """)

      st.markdown("### 🔹 Limpeza e Pré-processamento")
      st.write("""
      - 🚫 **Remoção de colunas geográficas redundantes**, como UF, município e capital, já que o estudo é focado apenas no DF.  
      - ✅ **Otimização da base** para tornar a análise mais **direcionada e eficiente**.  
      """)

      st.markdown("""
      ⚠ **Observação:** Durante o tratamento e análise, algumas variáveis poderão ser **excluídas** se forem consideradas **redundantes** ou de **baixa relevância** para os objetivos da pesquisa.  
      """)

  # ----------------------------------------------------------------------------
  # 🗂 Base de Dados Utilizada
  # ----------------------------------------------------------------------------
  with tab2:
      st.header("Base de Dados Utilizada")

      st.write("""
      Os dados utilizados neste estudo são os **microdados do Censo da Educação Superior**, fornecidos pelo **INEP**, cobrindo os anos de **2018 a 2023**.  
      Estes arquivos contêm informações detalhadas sobre os cursos de graduação ofertados no Brasil.
      """)

      st.markdown("### 🔹 Período da Análise")
      st.markdown("""
      - 📅 **Ano inicial:** 2018  
      - 📅 **Ano final:** 2023  
      - 🏛 **Fonte:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (**INEP**)  
      """)

      st.markdown("""
      ✔ **A amostra foi composta pelas 10 faculdades do DF mais bem avaliadas pelo MEC**. Isso significa que o estudo não engloba todas as instituições da região.  
      """)

  # ----------------------------------------------------------------------------
  # 🏫 Instituições Selecionadas
  # ----------------------------------------------------------------------------
  with tab3:
      st.header("Instituições Selecionadas")

      st.write("""
      Inicialmente, foram consideradas as **10 melhores instituições** de ensino superior do DF com **avaliação positiva pelo MEC**.  
      Mais adiante, a seleção foi reduzida para **6 instituições**, priorizando aquelas com **maior volume de cursos** e **dados mais completos**.
      """)

      st.markdown("### 🔹 Lista das Instituições Selecionadas")
      
      # Criando uma tabela formatada
      st.table([
          ["UNB", 769, "\~25%"],
          ["IESB", 478, "\~16%"],
          ["UCB", 452, "\~15%"],
          ["UNICEUB", 365, "\~12%"],
          ["UNIPROJEÇÃO", 230, "\~8%"],
          ["UDF", 215, "\~7%"]
      ])

  # ----------------------------------------------------------------------------
  # 🔍 Dados Faltantes e Duplicados
  # ----------------------------------------------------------------------------
  with tab4:
      st.header("Dados Faltantes e Duplicados")

      st.write("""
      Durante a etapa de pré-processamento dos dados, foram **identificados dados duplicados**, que foram devidamente tratados.  
      Além disso, foram detectados **140 registros com campos nulos**, concentrados nos anos **2018 e 2019**.
      """)

      st.markdown("### 🔹 Decisão sobre dados faltantes")
      st.write("""
      ❌ **Serão removidos os dados vazios dos anos de 2018 e 2019**, mantendo apenas os registros mais completos de **2020 a 2023**.  
      """)

      st.markdown("📊 Situação dos Dados:")
      st.table([
          ["2018", 456, 65, "14,25%"],
          ["2019", 494, 75, "15,18%"]
      ])

      st.write("""
      ✔ Mesmo com essa exclusão, **80% dos dados são preservados**, garantindo que a análise seja representativa.
      """)

  # ----------------------------------------------------------------------------
  # 📌 Ajustes e Transformações
  # ----------------------------------------------------------------------------
  with tab5:
      st.header("Ajustes e Transformações nas Colunas")

      st.write("""
      Durante o tratamento dos dados, algumas **colunas categóricas estavam registradas como números**, dificultando análises futuras.  
      Foram criados **dicionários de conversão**, que transformam essas categorias em descrições legíveis.
      """)

      st.markdown("### 🔹 Dicionários Criados para Transformação")
      st.code("""
      dic_TP_REDE = {1: "Pública", 2: "Privada"}

      dic_TP_GRAU_ACADEMICO = {
          1: "Bacharelado",
          2: "Licenciatura",
          3: "Tecnológico",
          0: "Não aplicável"
      }

      dic_IN_GRATUITO = {0: "Não", 1: "Sim"}

      dic_TP_MODALIDADE_ENSINO = {1: "Presencial", 2: "Curso a distância"}
      """, language="python")

      st.write("""
      ✔ **Essas transformações permitem que as análises fiquem mais fáceis de interpretar**, eliminando códigos numéricos abstratos.
      """)

  # ----------------------------------------------------------------------------
  # 🛠️ Normalização dos Dados
  # ----------------------------------------------------------------------------
  with tab6:
      st.header("Normalização dos Dados")

      st.write("""
      Para evitar inconsistências, os nomes de cursos passaram por uma normalização.  
      Foram corrigidas **variações de escrita**, **acentuação** e **padronização de formato**.
      """)

      st.markdown("### 🔹 Problemas Identificados")
      st.write("""
      - 📌 **Diferença de maiúsculas/minúsculas**  
      - 📌 **Acentuação inconsistente**  
      - 📌 **Nomes duplicados com pequenas variações**
      """)

      st.markdown("### 🔹 Exemplo de correção")
      st.code("""
      col_cor_NO_CURSO = {
          'LETRAS - PORTUGUES': 'LETRAS - LINGUA PORTUGUESA',
          'COMUNICACAO SOCIAL - JORNALISMO': 'JORNALISMO',
          'CIENCIA ECONOMICA': 'CIENCIAS ECONOMICAS'
      }
      """, language="python")

  # ----------------------------------------------------------------------------
  # 🔍 Análise Crítica
  # ----------------------------------------------------------------------------
  with tab7:
      st.header("Análise Crítica")

      st.write("""
      🎯 **Pontos positivos:**  
      - Temos **10 instituições diferentes**, garantindo diversidade.  
      - A **UNB tem mais de 700 registros**, possibilitando análises bem detalhadas.
      """)

      st.write("""
      ⚠ **Pontos de atenção:**  
      - **Distribuição não equilibrada**: Mais da metade dos dados está concentrada em **UNB, IESB e UCB**.  
      - **Instituições como IDP-BSB têm poucos registros**, o que pode tornar análises sobre elas menos confiáveis.
      """)

      st.write("""
      📌 **O que isso significa para a análise de evasão?**  
      - Focar **nas instituições com dados suficientes** (as 6 ou 7 maiores).  
      - Caso queira analisar a evasão em todo o DF, **deixar claro que há instituições com maior peso**, o que pode influenciar os resultados.
      """)
