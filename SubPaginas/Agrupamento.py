import streamlit as st

from SubPaginas.Global import *


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
    st.code("""
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
            """,language="python",line_numbers=True,wrap_lines=True)
    if st.button('Voltar para a página principal'):
        st.session_state.page = 'main'
