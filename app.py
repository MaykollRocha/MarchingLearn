import streamlit as st

from SubPaginas.Metricas import main as Metricas


def main_page():
    st.title("Maykoll Rocha - Tópicos em Aprendizagem de Máquina")
    st.markdown("""
            ### Introdução 
            
            A seguir irei apressentar conteudo trazio para mim em tópicos em aprendizagem de máquina uma matéria muito relevante para minha futura 
            vontade de vocação que será focada em análise de Dados.  
            Será sudivido em aparte as apresentações com a Side Bar ao lado. Nele terá os projetos que fiz e os códigos que implementei.
            """)

    
    if st.button('Metricas'):
        st.session_state.page = 'Metricas'
        
    
# Defina o estado da página se não estiver definido
if 'page' not in st.session_state:
    st.session_state.page = 'main'



# Controle de navegação
if st.session_state.page == 'main':
    main_page()
elif st.session_state.page == 'nrz':
    Metricas()
else:
    main_page()
    st.write("""
             Ainda está em desenvolvimento
             """)