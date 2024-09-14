import streamlit as st


def main():
    # Streamlit UI
    st.title('Metricas')
    st.markdown("""
                Comentar sobre as métricas de avaliação de um código.
                """)
    

   
    
    if st.button('Voltar para a página principal'):
        st.session_state.page = 'main'