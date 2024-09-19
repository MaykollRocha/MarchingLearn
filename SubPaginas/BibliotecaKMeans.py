import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


def simples_plot(title,data,rotulo):

    # Define o tamanho da figura com base nas entradas do usuário
    plt.figure(figsize=(10, 4))
    plt.title(f"{title}")
    plt.scatter(data[:,0], data[:,1], c=rotulo)
    return plt

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

def entropy(matriz, rotulo):
    """
    Calcula a entropia dos rótulos em uma matriz de dados.

    Parameters:
    - matriz (numpy.ndarray): Matriz de dados onde cada linha é um ponto.
    - rotulo (numpy.ndarray): Array com os rótulos ou classes dos pontos.

    Returns:
    - float: Entropia calculada.
    """
    entropia = 0
    total = len(matriz)
    for valor in np.unique(rotulo):
        proporcao = len(matriz[rotulo == valor]) / total
        if proporcao > 0:  # Evita o log de 0
            entropia -= proporcao * np.log2(proporcao)
    return entropia

def plot_Gráfico(matriz, clusters, rotulo, centroides, centroids_init):
    """
    Plota gráficos para visualização dos dados, mostrando a distribuição dos clusters e centroides.

    Parameters:
    - matriz (numpy.ndarray): Matriz de dados onde cada linha é um ponto.
    - clusters (numpy.ndarray): Array com os índices dos clusters para cada ponto.
    - rotulo (numpy.ndarray): Array com os rótulos ou classes dos pontos.
    - centroides (numpy.ndarray): Matriz final dos centroides.
    - centroids_init (numpy.ndarray): Matriz dos centroides iniciais.
    """
    # Cria uma figura com dois subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    # Subplot para os dados originais
    ax1.set_title("Original")
    ax1.scatter(matriz[:, 0], matriz[:, 1], c=rotulo, cmap='viridis')
    ax1.scatter(centroids_init[:, 0], centroids_init[:, 1], color='red', marker='*', s=100, alpha=1)
    
    # Subplot para a iteração final
    ax2.set_title("Final Iteration")
    ax2.scatter(matriz[:, 0], matriz[:, 1], c=clusters, cmap='viridis')
    ax2.scatter(centroides[:, 0], centroides[:, 1], color='red', marker='*', s=100, alpha=1)
    
    # Ajusta o layout dos subplots
    plt.tight_layout()
    return plt


# Distância Euclidiana:
dist_euclidiana = lambda prototipo, objeto: np.sqrt(np.sum((objeto - prototipo) ** 2, axis=1))

def int_centroides(matriz, k):
    """
    Inicializa os centroides selecionando aleatoriamente k pontos da matriz.

    Parameters:
    - matriz (numpy.ndarray): Matriz de dados onde cada linha é um ponto.
    - k (int): Número de centroides a serem inicializados.

    Returns:
    - centroides (numpy.ndarray): Matriz de centroides inicializados.
    """
    indices = np.random.choice(matriz.shape[0], k, replace=False)
    centroides = matriz[indices]
    return centroides

def atribuir_clusters(matriz, centroides):
    """
    Atribui cada ponto da matriz ao cluster mais próximo com base na distância euclidiana dos centroides.

    Parameters:
    - matriz (numpy.ndarray): Matriz de dados onde cada linha é um ponto.
    - centroides (numpy.ndarray): Matriz de centroides.

    Returns:
    - clusters (numpy.ndarray): Array onde cada elemento representa o índice do cluster atribuído a cada ponto.
    """
    distancias = np.zeros((matriz.shape[0], len(centroides)))
    for i, centroide in enumerate(centroides):
        distancias[:, i] = dist_euclidiana(centroide, matriz)
    clusters = np.argmin(distancias, axis=1)
    return clusters

def atualizar_centroides(matriz, clusters, k):
    """
    Atualiza os centroides calculando a média dos pontos em cada cluster.

    Parameters:
    - matriz (numpy.ndarray): Matriz de dados onde cada linha é um ponto.
    - clusters (numpy.ndarray): Array com os índices dos clusters para cada ponto.
    - k (int): Número de clusters.

    Returns:
    - centroides (numpy.ndarray): Matriz atualizada de centroides.
    """
    centroides = np.zeros((k, matriz.shape[1]))
    for i in range(k):
        pontos_cluster = matriz[clusters == i]
        if len(pontos_cluster) > 0:
            centroides[i] = np.mean(pontos_cluster, axis=0)
    return centroides

import matplotlib.pyplot as plt
import numpy as np


def k_means(matriz, k, max_iter=10):
    """
    Executa o algoritmo k-means para particionar a matriz em k clusters.

    Parameters:
    - matriz (numpy.ndarray): Matriz de dados onde cada linha é um ponto.
    - k (int): Número de clusters.
    - max_iter (int, opcional): Número máximo de iterações do algoritmo (padrão é 10).

    Returns:
    - centroides (numpy.ndarray): Matriz final de centroides após o algoritmo.
    - clusters (numpy.ndarray): Array com os índices dos clusters para cada ponto.
    - copy_of_init_centroids (numpy.ndarray): Cópia dos centroides iniciais.
    """
    # Inicializa os centroides
    centroides = int_centroides(matriz, k)
    copy_of_init_centroids = centroides.copy()
    
    for i in range(max_iter):
        # Atribui pontos aos clusters mais próximos
        clusters = atribuir_clusters(matriz, centroides)
        # Calcula os novos centroides
        novos_centroides = atualizar_centroides(matriz, clusters, k)
        
        plt.clf()  # Limpa a figura antes de desenhar nova iteração
        plt.title(f"Interação {i+1}")
        plt.scatter(matriz[:, 0], matriz[:, 1], c=clusters)
        plt.scatter(centroides[:, 0], centroides[:, 1], color='red', marker='*', s=100, alpha=1)
        plt.pause(0.1)  # Adiciona um pequeno atraso para visualização

        # Verifica se os centroides mudaram
        if np.all(centroides == novos_centroides):
            break

        centroides = novos_centroides
    
    st.pyplot(plt)
    return centroides, clusters, copy_of_init_centroids

