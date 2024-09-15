Normalizacos = {
    "Linear":{
        "Descrição":" Transforma os dados para um intervalo específico, geralmente [0, 1], preservando a distribuição original. Muito útil quando você sabe os valores máximos e mínimos de antemão.",
        "Formula":r"x' = \frac{x - x_{\text{min}}}{x_{\text{max}} - x_{\text{min}}}",
    },
    "Z-Score Scaling":{
        "Descrição":"Centraliza os dados em torno de uma média de 0 e desvio padrão de 1, sendo útil para dados com distribuições normais.",
        "Formula":r"z = \frac{x - \mu}{\sigma}",
    },
    " Max-Min":{
        "Descrição":"Cria os valores de acordo com um dadado espaço numerico do seu agrado por padrão é [0,1] porem pode ser um que seja definido pelo usuário.",
        "Formula":r"f(X) = \frac{X - min_X}{max_X - min_X} \times (novo\_max_X - novo\_min_X) + novo\_min_X",
    },
    "Valor Máximo":{
        "Descrição":"Escala os dados pelo valor absoluto máximo, mantendo a dispersão e lidando bem com dados esparsos.",
        "Formula":r"x' = \frac{x}{|x_{\text{max}}|}",
    },
 
}

#Funções Auxiliares
def media(daset):
    sum = 0
    cont = 0
    for i in daset:
        sum += i
        cont += 1
    return round(sum/cont,2)

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
    

def desvio_Padrao(data):
    med = media(data)
    sum = 0
    for i in data:
        sum += (i - med)**2
    return (sum/len(data))**0.5

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