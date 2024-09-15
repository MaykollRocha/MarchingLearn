import streamlit as st

from SubPaginas.Agrupamento import main as Agrupamento
from SubPaginas.Metricas import main as Metricas
from SubPaginas.PreProcessamento import main as PreProcess

st.set_page_config(
    page_title="Minha Aplicação",
    page_icon=":star:",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main_page():
    st.title("Tópicos em Aprendizagem de Máquina - Maykoll Rocha")
    st.markdown("""
    ### Introdução  
    Neste projeto, apresentarei conteúdos relacionados à disciplina de Aprendizado de Máquina, uma área essencial para a minha futura carreira, que será focada em Análise de Dados. O conteúdo será organizado de forma estruturada, com uma barra lateral para facilitar a navegação, onde você encontrará os projetos que desenvolvi e os códigos que implementei.  
    Quando falamos de **Machine Learning**, é importante seguir etapas fundamentais. A primeira é a definição do problema e a segunda é a coleta de dados. Embora este projeto não trate especificamente dessas etapas iniciais, o foco aqui será em métricas, explicando a importância de utilizá-las e mostrando os códigos que criei para aplicá-las. No entanto, vale ressaltar que as duas primeiras fases são cruciais para a aplicação real de **Machine Learning**.  
            """)
    st.markdown("""
            ### Pré-processamento dos Dados
            Uma etapa crucial após obter os dados é processá-los corretamente. Muitas vezes, utilizam-se mecanismos de ETL (Extração, Transformação e Carregamento) para preparar os dados de forma adequada para o negócio ou aplicação desejada. No entanto, durante esse processo, erros inesperados podem ocorrer, uma vez que o ETL não foca necessariamente na limpeza dos dados. É comum que, após essa etapa, ainda haja duplicatas, valores inconsistentes ou variáveis que precisam ser ajustadas, como a necessidade de normalização e padronização.  
            Por isso, o pré-processamento torna-se essencial para garantir que os dados estejam limpos e prontos para o uso em modelos de Machine Learning ou outras análises. Na próxima seção, abordaremos essas etapas detalhadamente.  
            """)
    

    if st.button('Pré Processamento'):
        st.session_state.page = 'preProcessamento'
    
    st.markdown("""
                ### Agrupamento de Dados

O agrupamento de dados é uma técnica de aprendizado não supervisionado que organiza um conjunto de dados em grupos ou clusters, onde os elementos dentro de cada grupo são mais semelhantes entre si do que com os de outros grupos. Essa abordagem é crucial para descobrir padrões e estruturas ocultas nos dados, permitindo uma análise mais aprofundada sem a necessidade de rótulos predefinidos.

Em machine learning, o agrupamento ajuda na segmentação de mercado, redução de dimensionalidade e detecção de anomalias. Ele também serve como um passo preliminar para outras técnicas, facilitando a personalização de recomendações e a exploração inicial dos dados. Ao revelar informações não evidentes e simplificar conjuntos de dados complexos, o agrupamento torna-se uma ferramenta essencial para obter insights valiosos e aprimorar a performance dos modelos de aprendizado de máquina.
                                
                """)
    
    if st.button("Agrupamento"):
        st.session_state.page = 'Agrupamento'
    
    
    
    
        
    
# Defina o estado da página se não estiver definido
if 'page' not in st.session_state:
    st.session_state.page = 'main'



# Controle de navegação
match st.session_state.page:
    case 'main': main_page()
    case 'Agrupamento': Agrupamento()
    case "preProcessamento":PreProcess()
    case _:
        main_page()
