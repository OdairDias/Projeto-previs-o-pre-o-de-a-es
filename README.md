# LSTM Projeto-previsão de preço de ações
   *Este projeto tem por objetivo, tentar prever o preço futuro de uma determinada ação
   levando em consideração os movimentos passados do ativo usando rede neural LSTM.
   Bibliotecas utilizadas:
   Bibliotecas principais: Tensorflow, Keras, scikit-learn
   Bibliotecas auxiliares: Pandas, Numpy,
   Sklearn, Matplotlib, Pandas datareader*


## O que é uma  Redes Long-Short Term Memory?
   *Em aprendizado profundo (Deep Learning), as Redes Neurais Recorrentes (RNNs) são Redes Neurais Artificiais que, diferentemente das redes neurais feedforward, usam 
    conexões reversas, onde os nós podem se conectar a outros nós nas camadas anteriores, ou a si mesmos, formando um ciclo direcionado. Como resultado, essas arquiteturas têm capacidade de memória, onde o valor passado do neurônio juntamente com a entrada da camada anterior, são a entrada do neurônio/camada. Portanto, os valores de saída passados do neurônio, são determinados pelas entradas passadas, influenciando sua saída atual. No nosso caso, utilizamos o preço de fechamento das ações como entrada e o preço de fechamento para treinar o modelo para que assim prever qual seria o preço fututo da ação escolhida*
    
![Rede LSTM](https://user-images.githubusercontent.com/117185803/202445443-a3a6fbe8-8cec-4099-ad73-3052e72d2385.jpg)



  *A baixo podemos verificar o resultado dos testes aplicados, utilizamos como referência 2019-01-01.Podemos verificar que o modelo conseguiu acompanhar de certa forma o preço real do ativo, estando o cálculo da Raiz do Erro Médio quadrado em 1.55.*


![grafico comparativo](https://user-images.githubusercontent.com/117185803/202303624-5ffcff86-72c5-4423-a9f1-fef90af89fad.png)
