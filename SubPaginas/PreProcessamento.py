
import streamlit as st


def main():
    st.title('Pré-processamento de Dados')
    
    st.markdown("""
    ### A Importância do Pré-processamento de Dados

    O pré-processamento de dados é uma etapa fundamental no desenvolvimento de modelos de **Machine Learning**. Antes de treinar qualquer modelo, os dados devem ser cuidadosamente preparados para garantir que estejam em um formato adequado para análise. Dados brutos costumam conter inconsistências, valores ausentes e variáveis irrelevantes, o que pode comprometer a precisão e a performance do modelo.  

    Ao realizar o pré-processamento, garantimos que os dados estejam limpos, consistentes e adequadamente transformados para atender aos requisitos específicos do algoritmo a ser utilizado. Esse processo é essencial para melhorar a qualidade dos dados, evitar erros durante o treinamento do modelo e, por fim, garantir resultados mais precisos e confiáveis.  

    A seguir, são descritas as etapas principais envolvidas no pré-processamento de dados.  

    ### Etapas do Pré-processamento de Dados

    1. **Limpeza de dados**:  
    Remoção de valores ausentes, duplicatas e outliers. Esse passo é crucial para evitar que dados incorretos ou distorcidos influenciem negativamente o modelo.  

    2. **Engenharia de características (Feature Engineering)**:  
    Criação ou seleção de características relevantes para melhorar o desempenho do modelo. Isso pode incluir transformar variáveis categóricas em numéricas, combinar variáveis existentes ou criar novas variáveis a partir dos dados disponíveis.
  
    3. **Transformação de dados**:  
    Ajuste dos dados por meio de normalização ou padronização, dependendo do algoritmo escolhido. A transformação garante que os dados estejam na mesma escala ou formato, facilitando a convergência do modelo e o processamento eficiente.
    
    """)
    
    if st.button('Voltar para a página principal'):
        st.session_state.page = 'main'