Normalizacos = {
    "Linear":{
        "Descrição":" Transforma os dados para um intervalo específico, geralmente [0, 1], preservando a distribuição original. Muito útil quando você sabe os valores máximos e mínimos de antemão.",
        "Formula":"x' = \frac{x - x_{\text{min}}}{x_{\text{max}} - x_{\text{min}}}",
    },
    "Z-Score Scaling":{
        "Descrição":"Valor Máximo",
        "Formula":"z = \frac{x - \mu}{\sigma}",
    },
    " Max-Min":{
        "Descrição":"Cria os valores de acordo com um dadado espaço numerico do seu agrado por padrão é [0,1] porem pode ser um que seja definido pelo usuário.",
        "Formula":"f(X) = \frac{X - min_X}{max_X - min_X} \times (novo\_max_X - novo\_min_X) + novo\_min_X",
    },
    "Valor Máximo":{
        "Descrição":"Escala os dados pelo valor absoluto máximo, mantendo a dispersão e lidando bem com dados esparsos.",
        "Formula":"x' = \frac{x}{|x_{\text{max}}|}",
    },
    "Robust Scaling":{
        "Descrição":"Subtrai a mediana e divide pelo intervalo interquartil (IQR), sendo robusto a outliers e útil para dados que não seguem distribuições normais.",
        "Formula":"x' = \frac{x - \text{mediana}(x)}{IQR(x)}",
    },
    "Decimal Scaling":{
        "Descrição":"Move os dados para uma escala onde o valor absoluto máximo está entre [0, 1]. É útil quando os dados variam em múltiplas ordens de grandeza.",
        "Formula":"x' = \frac{x}{10^j}",
    },
    "L2 Normalization":{
        "Descrição":"Escala os vetores de forma que sua norma 𝐿2 seja 1. Muito usada em métodos de aprendizado de máquina baseados em distância, como SVM e k-NN.",
        "Formula":"x' = \frac{x}{\sum |x_i|}",
    },
    "L1 Normalization":{
        "Descrição":"Normaliza os dados de forma que a soma dos valores absolutos de cada ponto seja igual a 1. Útil quando se lida com dados esparsos.",
        "Formula":"x' = \frac{x}{\sum |x_i|}",
    },
    "Logarithmic Transformation":{
        "Descrição":"Usada para lidar com dados que seguem uma distribuição exponencial, tornando-os mais normais. É sensível a valores próximos de zero, então frequentemente é adicionada uma constante.",
        "Formula":"x' = \log(x + 1)",
    },
    "Sigmoid Normalization":{
        "Descrição":"Mapeia os valores em um intervalo entre 0 e 1. É amplamente utilizada em redes neurais.",
        "Formula":"x' = \frac{1}{1 + e^{-x}}",
    },
    "Tanh Estimator Scaling ":{
        "Descrição":"Uma transformação robusta que mapeia os dados para o intervalo [0, 1], baseada na função tangente hiperbólica, útil em redes neurais profundas.",
        "Formula":"x' = 0.5 \times \left(1 + \tanh\left(0.01 \times (x - \mu)\right)\right)",
    },
    "Power Transformations":{
        "Descrição":"Generalização da Box-Cox para dados que contêm valores negativos. Essas transformações estabilizam a variância e tornam os dados mais gaussianos.",
        "Formula":"x' = \frac{x^{\lambda} - 1}{\lambda}",
    },
    
    
}