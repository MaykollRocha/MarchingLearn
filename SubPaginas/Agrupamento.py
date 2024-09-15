import matplotlib.pyplot as plt
import numpy as np
import requests
import streamlit as st

from SubPaginas.BibliotecaKMeans import *
from SubPaginas.Global import *


def simples_plot(title,data,rotulo):

    # Define o tamanho da figura com base nas entradas do usuário
    plt.figure(figsize=(10, 4))
    plt.title(f"{title}")
    plt.scatter(data[:,0], data[:,1], c=rotulo)
    return plt

def main():
    st.markdown("""
    # Introdução ao Agrupamento de Dados

    O agrupamento de dados, ou clustering, é uma técnica fundamental em aprendizado de máquina e análise de dados que busca organizar um conjunto de dados em grupos ou clusters, de modo que os elementos dentro de cada grupo sejam mais semelhantes entre si do que com os elementos de outros grupos. Essa técnica é amplamente utilizada em diversos contextos, desde segmentação de mercado até análise de padrões em grandes volumes de dados.

    O objetivo principal do agrupamento é identificar estruturas ou padrões subjacentes nos dados que não são imediatamente evidentes. Em vez de utilizar rótulos pré-definidos para os dados, o agrupamento permite que a estrutura dos dados revele informações significativas, tornando-o uma técnica não supervisionada. Isso significa que o modelo de agrupamento trabalha apenas com as características dos dados para formar os clusters, sem a necessidade de supervisão externa ou rótulos.

    ## Importância do Agrupamento de Dados em Machine Learning

    1. **Descoberta de Padrões e Estruturas**: O agrupamento é essencial para identificar padrões ou estruturas ocultas nos dados. Por exemplo, em marketing, pode-se usar agrupamento para segmentar clientes com comportamentos semelhantes, permitindo estratégias de marketing mais direcionadas e eficazes.

    2. **Redução de Dimensionalidade**: Ao agrupar dados semelhantes, é possível reduzir a complexidade dos dados. Esse processo simplifica o conjunto de dados e facilita a visualização e a análise subsequente. Técnicas como PCA (Análise de Componentes Principais) muitas vezes utilizam agrupamento como um pré-processamento para identificar as variáveis mais significativas.

    3. **Pré-processamento de Dados**: O agrupamento pode ser utilizado como uma etapa de pré-processamento para outras técnicas de aprendizado de máquina. Por exemplo, ao segmentar dados em clusters, é possível aplicar modelos diferentes para cada cluster, melhorando a performance geral do sistema.

    4. **Detecção de Anomalias**: Técnicas de agrupamento também são usadas para identificar anomalias ou outliers, que são dados que não se encaixam bem em nenhum cluster. Isso é útil em áreas como detecção de fraudes e monitoramento de sistemas para identificar comportamentos incomuns.

    5. **Exploração de Dados**: O agrupamento é uma ferramenta valiosa para a exploração inicial dos dados. Ele ajuda a formar hipóteses e direcionar a análise mais aprofundada, oferecendo insights que podem guiar decisões e estratégias.

    6. **Personalização e Recomendação**: Em sistemas de recomendação, o agrupamento pode ser utilizado para identificar grupos de usuários com interesses semelhantes e fornecer recomendações personalizadas com base nas preferências do grupo.

    Em resumo, o agrupamento de dados é uma técnica crucial para entender e explorar dados complexos e volumosos, oferecendo insights valiosos e facilitando a aplicação de modelos de aprendizado de máquina mais eficazes. Sua capacidade de revelar padrões e estruturas ocultas torna-o uma ferramenta indispensável para cientistas de dados e profissionais de machine learning.
                     
                """)
    
    st.markdown(r"""
## Numeros de Formas  
Para calcular o número de formas distintas de agrupar $( n )$ objetos em $( k )$ grupos, você está lidando com um problema que envolve a contagem de particionamentos de um conjunto. A fórmula que você forneceu é uma expressão baseada na **fórmula de Bell** para o número de particionamentos, ajustada por um fator para considerar o número de grupos específicos.  

### Fórmula  

A fórmula apresentada é:  

$$
P(n, k) = \frac{1}{k!} \sum_{j=1}^{k} (-1)^{k-j} \binom{k}{j} j^n 
$$

onde:
- $( P(n, k) )$ é o número de formas distintas de agrupar $( n )$ objetos em $( k )$ grupos.
- $( \binom{k}{j} )$ é o coeficiente binomial que representa o número de maneiras de escolher $( j )$ grupos entre $( k )$.
- $( j^n )$ representa o número de maneiras de distribuir $( n )$ objetos em $( j )$ grupos.
- O fator $( \frac{1}{k!} )$ corrige para as permutações dos grupos, para garantir que cada agrupamento seja contado apenas uma vez.

### Complexidade Computacional

O cálculo de $( P(n, k) )$ pode ser computacionalmente intensivo para grandes valores de $( n )$ e $( k )$, devido à necessidade de calcular potências e coeficientes binomiais. A complexidade computacional depende de como esses cálculos são realizados, geralmente envolvendo operações exponenciais e fatoriais. No entanto, para valores pequenos de $( n )$ e $( k )$, a fórmula é prática e fornece o número exato de particionamentos distintos possíveis.
                """)
    st.code(r'''
# Função para calcular o fatorial de um número
fat = lambda n: 1 if n == 0 else n * fat(n-1)

# Função para calcular o coeficiente binomial (combinação)
arj = lambda n, k: fat(n) / (fat(k) * fat(n - k))

def possibilidades(n, k):
    """
    Calcula o número de possibilidades de k objetos em n posições com repetição,
    usando o princípio de inclusão-exclusão.

    Parameters:
    - n (int): Número total de posições.
    - k (int): Número total de objetos.

    Returns:
    - float: Número de possibilidades.
    """
    return (1 / fat(k)) * sum([((-1) ** (k - j)) * arj(k, j) * (j ** n) for j in range(1, k + 1)])
            ''',language="python",line_numbers=True,wrap_lines=True)
    
    
    st.markdown('''
            ## Objetivos e Características do Agrupamento de Dados

            O agrupamento de dados é uma técnica essencial em análise de dados que visa identificar e descrever grupos naturais dentro de um conjunto de dados não rotulado. Aqui estão alguns dos principais objetivos e características dessa técnica:

            1. **Trabalho com Dados Não Rotulados**: No agrupamento, os dados não possuem rótulos predefinidos que indiquem a que grupo ou classe pertencem. O objetivo é descobrir essas classes ou grupos com base nas características dos dados.

            2. **Identificação e Descrição de Grupos**: Algoritmos de agrupamento são utilizados para identificar grupos de objetos semelhantes e descrever as características desses grupos. Cada objeto é representado como um ponto em um espaço vetorial, onde a dimensão do espaço é determinada pelo número de atributos do objeto.

            3. **Uso de Protótipos**: Alguns métodos de agrupamento utilizam protótipos, que são vetores representativos para cada grupo. Esses protótipos ajudam a reduzir o tamanho da base de dados e o custo de processamento, além de facilitar a análise das características dos grupos. Protótipos geralmente são posicionados no centro dos grupos ou em regiões de alta densidade, maximizando a representatividade dos objetos agrupados.

            4. **Redução e Representatividade**: O uso de protótipos permite condensar grandes quantidades de dados em um número menor de representações, mantendo a integridade das informações. Isso ajuda a simplificar a análise e interpretar os grupos encontrados de forma mais eficiente.

            5. **Descoberta de Grupos Naturais**: O objetivo final do agrupamento é identificar grupos naturais dentro dos dados. Esses grupos representam padrões ou estruturas subjacentes que podem fornecer insights valiosos sobre a base de dados.

            Em resumo, o agrupamento busca explorar dados não rotulados para identificar e entender padrões ocultos, utilizando métodos que podem incluir a criação de protótipos para facilitar a análise e interpretação dos resultados.
                
            ## Grupos Naturais

            Grupos naturais são definidos por dois critérios principais, conforme descrito por Carmichael (1968):

            1. **Regiões Contínuas e Densas**: Existem regiões contínuas no espaço de dados que são relativamente densamente povoadas por objetos. Essas regiões formam agrupamentos de objetos que são mais numerosos e próximos uns dos outros do que com objetos fora da região.

            2. **Áreas Relativamente Vazias**: As regiões densas estão rodeadas por áreas do espaço que são relativamente vazias. Isso significa que há uma clara separação entre os grupos, com poucas ou nenhuma interseção significativa entre as regiões densas e as regiões ao redor.

            Esses grupos naturais representam padrões subjacentes nos dados e são úteis para a análise e interpretação dos dados, ajudando a identificar estruturas e relações significativas.    
                
                ''')
    # Baixa os dados dos arquivos
    data_response = requests.get('https://raw.githubusercontent.com/MaykollRocha/Data_Sets/main/data.txt')
    rotulo_response = requests.get('https://raw.githubusercontent.com/MaykollRocha/Data_Sets/main/rotulos.txt')

    # Carrega os dados no NumPy
    data = np.loadtxt(data_response.text.splitlines())
    rotulo = np.loadtxt(rotulo_response.text.splitlines())
    
    st.plotly_chart(simples_plot("Base de Dados Tratada",data,rotulo), theme="streamlit")
    
    if st.button('Voltar para a página principal'):
        st.session_state.page = 'main'
