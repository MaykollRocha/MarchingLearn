
import numpy as np
import pandas as pd
import requests
import streamlit as st


def load_data():
    df = pd.read_csv(requests.get("https://github.com/MaykollRocha/Data_Sets/blob/main/Funcionarios%20(2).xlsx"))
    return df


df = load_data()

# Show a multiselect widget with the genres using `st.multiselect`.
genres = st.multiselect(
    "Genres",
    df.genre.unique(),
    ["Action", "Adventure", "Biography", "Comedy", "Drama", "Horror"],
)

# Show a slider widget with the years using `st.slider`.
years = st.slider("Years", 1986, 2006, (2000, 2016))

# Filter the dataframe based on the widget input and reshape it.
df_filtered = df[(df["genre"].isin(genres)) & (df["year"].between(years[0], years[1]))]
df_reshaped = df_filtered.pivot_table(
    index="year", columns="genre", values="gross", aggfunc="sum", fill_value=0
)
df_reshaped = df_reshaped.sort_values(by="year", ascending=False)


# Display the data as a table using `st.dataframe`.
st.dataframe(
    df_reshaped,
    use_container_width=True,
    column_config={"year": st.column_config.TextColumn("Year")},
)

# Display the data as an Altair chart using `st.altair_chart`.
df_chart = pd.melt(
    df_reshaped.reset_index(), id_vars="year", var_name="genre", value_name="gross"
)
chart = (
    alt.Chart(df_chart)
    .mark_line()
    .encode(
        x=alt.X("year:N", title="Year"),
        y=alt.Y("gross:Q", title="Gross earnings ($)"),
        color="genre:N",
    )
    .properties(height=320)
)

def Metricas():
    pass

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

    2. **Transformação de dados**:  
    Ajuste dos dados por meio de normalização ou padronização, dependendo do algoritmo escolhido. A transformação garante que os dados estejam na mesma escala ou formato, facilitando a convergência do modelo e o processamento eficiente.

    3. **Engenharia de características (Feature Engineering)**:  
    Criação ou seleção de características relevantes para melhorar o desempenho do modelo. Isso pode incluir transformar variáveis categóricas em numéricas, combinar variáveis existentes ou criar novas variáveis a partir dos dados disponíveis.
    """)
    
    st.altair_chart(chart, use_container_width=True)

    
    if st.button('Voltar para a página principal'):
        st.session_state.page = 'main'