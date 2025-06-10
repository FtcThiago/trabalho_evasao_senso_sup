import streamlit as st

def exibir():
    # Título principal
    st.title("📊 Conclusão Geral da Análise – Matrículas x Concluintes no Ensino Superior (2018–2023)")

    # Criando um seletor para explorar diferentes pontos da análise
    tema = st.selectbox(
        "🔍 Escolha um aspecto para explorar:",
        [
            "Visão Geral",
            "Diferenças por Gênero",
            "Desigualdade Racial",
            "Educação ao Longo da Vida",
            "Evasão por Curso",
            "Políticas de Permanência"
        ]
    )

    # Exibindo conteúdo baseado na escolha do usuário
    if tema == "Visão Geral":
        st.write("""
        A análise dos dados entre os anos de **2018 a 2023** revela um cenário preocupante e multifacetado sobre a trajetória dos estudantes no ensino superior. 
        Nota-se um **aumento contínuo nas matrículas**, indicando maior acesso à universidade, mas esse crescimento não tem sido acompanhado por um aumento proporcional nos concluintes. 
        Isso aponta para uma **taxa significativa de evasão** ao longo dos cursos.
        """)

    elif tema == "Diferenças por Gênero":
        st.write("""
        **Homens** têm uma taxa de conclusão menor em comparação às **mulheres**, mesmo sendo maioria em cursos como Computação e Tecnologia da Informação. 
        Já nas áreas da Saúde e Bem-Estar, há **predominância feminina** nas matrículas e uma **taxa de conclusão ligeiramente maior**.
        Esse padrão sugere uma **associação entre gênero e áreas de interesse**, mas também levanta questões sobre barreiras específicas enfrentadas por cada grupo.
        """)

    elif tema == "Desigualdade Racial":
        st.write("""
        **Pretos, pardos, indígenas e amarelos** estão sub-representados entre os concluintes, especialmente em comparação à população branca. 
        A média de concluintes **pretos** por curso é de apenas **2**, frente a **14 brancos** e **17 pardos**. 
        Isso evidencia uma **desigualdade estrutural**, refletindo falta de apoio, políticas de permanência e acessibilidade ao longo dos cursos.
        """)

    elif tema == "Educação ao Longo da Vida":
        st.write("""
        A participação de pessoas com **mais de 60 anos** no ensino superior é mínima. 
        A média de concluintes nessa faixa etária é **praticamente nula**, o que demonstra desafios sérios para uma **educação inclusiva e ao longo da vida**. 
        Ainda há barreiras que impedem o acesso pleno de adultos mais velhos ao ambiente universitário.
        """)

    elif tema == "Evasão por Curso":
        st.write("""
        Alguns cursos apresentam melhores índices de retenção, como **Formação de Professores e áreas de Terapia e Promoção da Saúde**. 
        Por outro lado, cursos como **Computação, Engenharia, Administração e Direito** mostram um padrão de **grande evasão**. 
        Isso indica que a evasão não ocorre de forma homogênea e que **diferentes áreas podem precisar de estratégias específicas de apoio**.
        """)

    elif tema == "Políticas de Permanência":
        st.write("""
        O aumento nas **matrículas** representa um avanço, mas sem políticas eficazes de **permanência, acessibilidade e suporte emocional, pedagógico e financeiro**, 
        muitos estudantes **não conseguem concluir seus cursos**. 
        O ensino superior precisa garantir que a inclusão vá além do ingresso, oferecendo apoio para que mais alunos cheguem à conclusão.
        """)

    # Rodapé com mensagem final
    st.write("💡 Para reduzir a evasão e tornar a educação superior mais inclusiva")