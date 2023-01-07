# Rede neural LSTM Projeto-previsão de preço de ações
   *Este projeto tem por objetivo, tentar prever o preço futuro de uma determinada ação
   levando em consideração os movimentos passados do ativo usando rede neural LSTM.
   Bibliotecas principais: Tensorflow, Keras, scikit-learn
   Bibliotecas auxiliares: Pandas, Numpy,
   Sklearn, Matplotlib, Pandas datareader*


## O que é uma  Rede LSTM ? (Long-Short Term Memory)
![Rede LSTM](https://user-images.githubusercontent.com/117185803/202445443-a3a6fbe8-8cec-4099-ad73-3052e72d2385.jpg)

   *Em aprendizado profundo (Deep Learning), as Redes Neurais Recorrentes (RNNs) são Redes Neurais Artificiais que, diferentemente das redes neurais feedforward, usam 
    conexões reversas, onde os nós podem se conectar a outros nós nas camadas anteriores, ou a si mesmos, formando um ciclo direcionado. Como resultado, essas arquiteturas têm capacidade de memória, onde o valor passado do neurônio juntamente com a entrada da camada anterior, são a entrada do neurônio/camada. Portanto, os valores de saída passados do neurônio, são determinados pelas entradas passadas, influenciando sua saída atual. No nosso caso, utilizamos o preço de fechamento das ações como entrada e o preço de fechamento para treinar o modelo para que assim prever qual seria o preço fututo da ação escolhida.*
    
  ### Consideração relevante 01:
Este estudo tem como foco principal, demostrar o potêncial das redes nêurais em especial LSTM. O modelo ficou bem estimado, porém ainda tem muito caminho a percorrer quanto a aplicação na bolsa de valores, pois temos algumas restriçoes, para prever o preço para os proximos dias, o modelo já conhecia de antemão os valores que háviam ocorrido naqueles dias que ele estava estimando, sendo assim ficou mais facil para o modelo "prever" os valores.

  ### Consideração relevante 02:
*Por mais que tenha suas limitações, podemos evoluir o modelo cada vez mais para que possa auxiliar na tomada de decisão, pois varias coisas podem afetar o preço de uma ação, podendo o modelo estimado ser um forte indicador de tendência ou direção pra onde o ativo pode se movimentar. O modelo apresentado, pode rodar qualquer ativo desde que tenha série histórica, modelo também pode ser desenvolvido para períodos menores como sessenta minutos, meia hora, enfim outros tempos gráficos. Recomenda-se antes de tomar qualquer decisão de investir ou não em um ativo, fazer suas próprias análises ou procurar acessoria especializada, pois o mercado de bolsa de valores apresenta riscos, onde dependendo da operação, pode-se perder mais do que o capital investido. O mercado de Bolsa de valores está bem evoluido em termos de tecnologia e automoção, o que temos de mais eficiênte e usado pelas grandes instituições são os HFT´s (high-frequency trading) que são robôs que trabalham em alta frequência com o objetivo de ganhar os pequenos spreds em cada opereção realizada, fazem isso milhares de vezes por dia.*


### Resultados:

  *A baixo podemos verificar o resultado dos testes aplicados, utilizamos como referência 2019-01-01.Podemos verificar que o modelo consegiu prever de maneira satisfatória o preço real do ativo, o que mostra que o modelo está bem ajustado, para o exemplo a baixo, o cálculo da Raiz do Erro Médio quadrado estava 1.55, o que é considerado satisfatório para o modelo.*


![grafico comparativo](https://user-images.githubusercontent.com/117185803/202303624-5ffcff86-72c5-4423-a9f1-fef90af89fad.png)

