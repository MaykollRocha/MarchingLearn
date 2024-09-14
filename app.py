from io import StringIO

import dropbox
import streamlit as st

from SubPaginas.Metricas import main as Metricas
from SubPaginas.PreProcessamento import main as PreProcess


def main_page():
    st.title("Maykoll Rocha - Tópicos em Aprendizagem de Máquina")
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
            ### Pré-processamento dos Dados
            Uma etapa crucial após obter os dados é processá-los corretamente. Muitas vezes, utilizam-se mecanismos de ETL (Extração, Transformação e Carregamento) para preparar os dados de forma adequada para o negócio ou aplicação desejada. No entanto, durante esse processo, erros inesperados podem ocorrer, uma vez que o ETL não foca necessariamente na limpeza dos dados. É comum que, após essa etapa, ainda haja duplicatas, valores inconsistentes ou variáveis que precisam ser ajustadas, como a necessidade de normalização e padronização.  
            Por isso, o pré-processamento torna-se essencial para garantir que os dados estejam limpos e prontos para o uso em modelos de Machine Learning ou outras análises. Na próxima seção, abordaremos essas etapas detalhadamente.  
            """)
    
    if st.button('Metricas'):
        st.session_state.page = 'Metricas'
        


    # Configurar o token de acesso do Dropbox
    DROPBOX_ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
    dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)

    # Função para baixar o arquivo do Dropbox
    def download_file_from_dropbox(path):
        _, res = dbx.files_download(path)
        return res.content.decode('utf-8')

    # Interface do Streamlit
    st.title('Leitor de Arquivo Dropbox')

    # Caminho do arquivo no Dropbox
    dropbox_path = st.text_input('Digite o caminho do arquivo no Dropbox')

    if dropbox_path:
        try:
            file_content = download_file_from_dropbox(dropbox_path)
            st.text_area('Conteúdo do Arquivo', file_content, height=300)
        except Exception as e:
            st.error(f'Ocorreu um erro: {e}')
            
        
    
# Defina o estado da página se não estiver definido
if 'page' not in st.session_state:
    st.session_state.page = 'main'



# Controle de navegação
match st.session_state.page:
    case 'main': main_page()
    case 'Metricas': Metricas()
    case "preProcessamento":PreProcess()
    case _:
        main_page()
