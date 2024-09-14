import pandas as pd
import streamlit as st


def load_data():

    df = pd.read_csv("data/Funcionarios.csv") 
    
    return df

def clear_data():
    dfPoor = load_data()
    #Retirar o dado igual a nutnull pois a dados que não tem como estimar facilmente
    df = dfPoor[dfPoor['cargo'].notnull()]
    #Retirando duplicatas
    df = df[dfPoor.duplicated() == False]
    #Retirar colunas que são irrelevantes para a analise
    df = df.drop(columns=['matricula','nome'])
    #caso algum dado de alguma coluna numerica esteja none use essa função ela preenche com moda desse gráfico
    df['num_filhos'] = df['num_filhos'].fillna(df['num_filhos'].mode()[0]) # Substituir valores None pela moda
    
    #caso tenha uma coluna que prescise trocar masculi ou feminimo
    df['sexo'] = df['sexo'].apply(lambda letra: 1 if letra[0].lower() == "m" else 0)
    df['estado_civil'] = df['estado_civil'].apply(lambda letra: 0 if letra[0].lower() == "s" else 1 if letra[0].lower() == "c" else 2 if letra[0].lower() == "d" else 3)
    df['cargo'] = pd.Categorical(df['cargo']).codes
    return df
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
    st.markdown("""
                # Abrindo Data-Frame
                Para demonstrar a limpeza e dar umas dicas vou abrir um data frame genérico que foi dada a min durante a matéria demostrar umas funções do padna apara limpa-lo com velocidade depois uma função apra tornar tudo nuemrico seguindo uma certa onde de classe.
                Inciamos abrindo o data frame:
                """)
    st.dataframe(load_data())
    st.code("""
            #Caso vôce precise limpar duplicatas ou valores null em coluna específica
            #Retirar o dado igual a nutnull pois a dados que não tem como estimar facilmente
            df = df[df['<Nome_da_coluna>'<caso queria por mais colunas ,'<Nome_da_coluna2>',...>].notnull()]
            #Retirando duplicatas
            df = df[df.duplicated() == False]
            #Retirar colunas que são irrelevantes para a analise
            df = df.drop(columns=['<Nome_da_coluna>',<caso queria por mais colunas ,'<Nome_da_coluna2>',...>])
            
            #Em casos de sexo muitas vezes eles coloca masculino e feminimo no codigo apresentou varias formar de escrever mas todas como com a mesma letra logo
            #caso tenha uma coluna que prescise trocar masculi ou feminimo
            df['sexo'] = df['sexo'].apply(lambda letra: 1 if letra[0].lower() == "m" else 0)
            #Esse proximo é para estado civil
            df['estado_civil'] = df['estado_civil'].apply(lambda letra: 0 if letra[0].lower() == "s" else 1 if letra[0].lower() == "c" else 2 if letra[0].lower() == "d" else 3)
            
            #Em uma coluna númerica quando tem um null podemos usar a moda para altera isso
             #caso algum dado de alguma coluna numerica esteja none use essa função ela preenche com moda desse gráfico
            df['<Nome_da_coluna>'] = df['<Nome_da_coluna>'].fillna(df['<Nome_da_coluna>'].mode()[0]) # Substituir valores None pela moda
            
            """,language='python')
    st.markdown("""## Clear data""")
    st.dataframe(clear_data())
    
    if st.button('Voltar para a página principal'):
        st.session_state.page = 'main'