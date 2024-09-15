Normalizacos = {
    "Linear":{
        "Descrição":r"""
A normalização min-max transforma os dados para que todos os valores estejam em um intervalo fixo. É especialmente útil quando você precisa garantir que os dados estejam em uma faixa específica para algoritmos que são sensíveis à escala, como redes neurais ou algoritmos baseados em distância.

### Fórmula

A fórmula para a normalização min-max é:

$$
x_{\text{norm}} = \frac{x - \text{min}(X)}{\text{max}(X) - \text{min}(X)}
$$

Onde:
- $( x_{\text{norm}} )$ é o valor normalizado,
- $\( x \)$ é o valor original,
- $\(\text{min}(X)\)$ é o valor mínimo do conjunto de dados $\(X\)$,
- $\(\text{max}(X)\)$ é o valor máximo do conjunto de dados $\(X\)$.

### Interpretação

- **Valores entre 0 e 1**: Após a normalização, todos os valores estarão entre 0 e 1, onde 0 corresponde ao valor mínimo e 1 corresponde ao valor máximo do conjunto de dados original.
- **Valores fora da faixa**: Se o valor original estiver fora do intervalo \([\text{min}(X), \text{max}(X)]\), o valor normalizado pode ficar fora do intervalo \([0, 1]\), mas isso geralmente não ocorre se o intervalo é bem definido e os dados estão dentro do intervalo original.
         """,
        "Code":"""
def Nomraliza_Linear(data):
    for i in data:
        data[i] = (data[i] - data[i].min())/(data[i].max() - data[i].min())
    return data
"""
    },
    "Z-Score Scaling":{
        "Descrição":r"""
    Centraliza os dados em torno de uma média de 0 e desvio padrão de 1, sendo útil para dados com distribuições normais.   
    $$ 
    z = \frac{x - \mu}{\sigma} 
    $$  
    Onde:
    - $(x)$ é o valor individual,
    - $(\mu)$ é a média do conjunto de dados,
    - $(\sigma)$ é o desvio-padrão.

    ### Interpretação dos valores de z-score:
    - **Valores positivos**: Significam que o valor \(x\) está **acima da média**.
    - **Valores negativos**: Significam que o valor \(x\) está **abaixo da média**.
    - **z = 0**: Significa que o valor está **igual à média**.
        """,
        "Code":"""
def media(dataset):
    sum = 0
    cont = 0
    for i in dataset:
        sum += i
        cont += 1
    return round(sum / cont, 2)

def desvio_padrao(data):
    med = media(data)
    sum = 0
    for i in data:
        sum += (i - med) ** 2
    return (sum / len(data)) ** 0.5

def normaliza_scoreZ(data):
    med = media(data)
    desvio = desvio_padrao(data)
    return [(x - med) / desvio for x in data]     
        
        """
    },
    " Max-Min":{
        "Descrição":r"""
A normalização Min-Max reescalona os valores dos dados para um intervalo específico. Por padrão, esse intervalo é geralmente \([0, 1]\), mas pode ser definido pelo usuário para qualquer intervalo desejado.

### Fórmula

A fórmula para a normalização Min-Max com um intervalo de saída personalizado é:

$$
f(X) = \frac{X - \text{min}_X}{\text{max}_X - \text{min}_X} \times (\text{novo\_max}_X - \text{novo\_min}_X) + \text{novo\_min}_X
$$

Onde:
- $\( X \)$ é o valor original,
- $\(\text{min}_X\)$ é o valor mínimo do conjunto de dados original,
- $\(\text{max}_X\)$ é o valor máximo do conjunto de dados original,
- $\(\text{novo\_min}_X\)$ é o novo valor mínimo desejado para o intervalo,
- $\(\text{novo\_max}_X\)$ é o novo valor máximo desejado para o intervalo.

### Interpretação

- **Intervalo Personalizado**: Você pode ajustar \(\text{novo\_min}_X\) e \(\text{novo\_max}_X\) para definir o intervalo de saída desejado. Por exemplo, se você quiser que os valores normalizados estejam entre 10 e 20, defina \(\text{novo\_min}_X = 10\) e \(\text{novo\_max}_X = 20\).
- **Transformação Linear**: A fórmula aplica uma transformação linear aos dados para ajustá-los ao novo intervalo.
        """,
        "Code":"""
def Nomraliza_MaxMin(data,nMn =[0,1]):
    for i in data:
        data[i] = (data[i] - data[i].min())/(data[i].max() - data[i].min())*(nMn[1]-nMn[0]) + nMn[0]
    return data
        """
    },
    "Valor Máximo":{
        "Descrição":r"""
Essa técnica escala os dados dividindo cada valor pelo valor absoluto máximo do conjunto de dados. Isso garante que o valor máximo seja ajustado para 1 (ou -1, dependendo do sinal) e preserva a relação relativa entre os valores.

### Fórmula

A fórmula para a normalização pelo valor máximo é:

$$
x' = \frac{x}{|x_{\text{max}}|}
$$

Onde:
- $\( x' \)$ é o valor normalizado,
- $\( x \)$ é o valor original,
- $\( |x_{\text{max}}| \)$ é o valor absoluto do maior valor absoluto no conjunto de dados.

### Interpretação

- **Escalamento Relativo**: A normalização pelo valor máximo preserva a dispersão dos dados, pois todos os valores são escalados em relação ao valor máximo absoluto do conjunto de dados.
- **Manutenção da Dispersão**: Essa técnica é útil para dados esparsos e ajuda a manter a estrutura dos dados sem distorcer a dispersão relativa.
        """,
        "Code":"""
def Nomraliza_ValorMax(data):
    for i in data:
        data[i] = data[i]/data[i].max()
    return data
        
        """
    },
 
}


def moda(daset):
    mod ={}
    for i in daset:
        if i in mod:
            mod[i] += 1
        else:
            mod[i] = 1
    moda = max(mod,key=mod.get)
    return moda

def mediana(data):
    sorted_data = sorted(data)
    return  (sorted_data[len(data)//2 - 1] + sorted_data[len(data)//2]) / 2 if len(data) % 2 == 0 else sorted_data[len(data)//2]
    

def media(dataset):
    sum = 0
    cont = 0
    for i in dataset:
        sum += i
        cont += 1
    return round(sum / cont, 2)

def desvio_Padrao(data):
    med = media(data)
    sum = 0
    for i in data:
        sum += (i - med) ** 2
    return (sum / len(data)) ** 0.5


#Normalizações 

def Nomraliza_Linear(data):
    for i in data:
        data[i] = (data[i] - data[i].min())/(data[i].max() - data[i].min())
    return data

def Nomraliza_ScoreZ(data):
    for i in data:
        data[i] = (data[i] - media(data[i]))/desvio_Padrao(data[i])
    return data

def Nomraliza_MaxMin(data,nMn =[0,1]):
    for i in data:
        data[i] = (data[i] - data[i].min())/(data[i].max() - data[i].min())*(nMn[1]-nMn[0]) + nMn[0]
    return data

def Nomraliza_ValorMax(data):
    for i in data:
        data[i] = data[i]/data[i].max()
    return data