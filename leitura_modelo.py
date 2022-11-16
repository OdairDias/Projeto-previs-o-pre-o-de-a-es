from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas_datareader as dados
import pandas as pd
import numpy as np
#
ativo = "PETR4.SA"  # https://finance.yahoo.com/
# iremos colocar data inicial, sistema irá buscar até o dia atual
dados_do_ativo = dados.DataReader(ativo, start="2019-01-01", data_source='yahoo')
import matplotlib.pyplot as plt
#plt.style.use('fivethirtyeight')
# plt.style.use('default')
plt.figure(figsize=(16,8))
plt.title('Histórico de fechamento ' + ativo)
plt.plot(dados_do_ativo['Close'])
plt.xlabel('Data')
plt.ylabel('Preço de fechamento')
#plt.show()
# preparação dos dados
cotacoes_df = dados_do_ativo.filter(['Close'])
cotacoes = cotacoes_df.values
from sklearn.preprocessing import MinMaxScaler
normalizador = MinMaxScaler(feature_range=(0, 1)) 
cotacoes_normalizadas = normalizador.fit_transform(cotacoes)
# separando dados para aprendizado
from math import ceil
dias_treinamento = ceil( len(cotacoes) *.8) 
cotacoes_treinamento = cotacoes_normalizadas[0:dias_treinamento]
x_treino=[]
y_treino = []
for i in range(30,len(cotacoes_treinamento)):
    x_treino.append(cotacoes_treinamento[i-30:i])
    y_treino.append(cotacoes_treinamento[i])

x_treino, y_treino = np.array(x_treino), np.array(y_treino)
x_treino = np.reshape(x_treino, (len(x_treino),30,1))
# Criando Modelo:
from keras.models import Sequential
from keras.layers import Dense, LSTM
model = Sequential()
model.add(LSTM(units=70, return_sequences=True,input_shape=(30,1)))
model.add(LSTM(units=70, return_sequences=False))
model.add(Dense(units=25))
model.add(Dense(units=1))
model.compile(optimizer='adam', loss='mean_squared_error')
# treinamento modelo
model.fit(x_treino, y_treino, batch_size=1, epochs=1)
# separação e preparação dados para teste
cotacoes_teste = cotacoes_normalizadas[dias_treinamento - 30:]
x_teste = []
y_teste =  cotacoes[dias_treinamento:] 
for i in range(30,len(cotacoes_teste)):
    x_teste.append(cotacoes_teste[i-30:i])
x_teste = np.array(x_teste)
x_teste = np.reshape(x_teste, (len(x_teste),30,1))
# teste predição:
predictions = model.predict(x_teste) 
predictions = normalizador.inverse_transform(predictions)
## Calculo da Raiz do Erro Médio Quadrado (RMSE)
rmse=np.sqrt(np.mean(((predictions- y_teste)**2)))
rmse
print(rmse)
# grafico comparativo:
treino = cotacoes_df[:dias_treinamento]
valido = cotacoes_df[dias_treinamento:]
valido['Predictions'] = predictions
plt.figure(figsize=(15,7))
plt.title('Ativo ' + ativo)
plt.xlabel('Data')
plt.ylabel('Preço de fechamento (R$)')
plt.plot(treino['Close'], color = 'black')
plt.plot(valido['Close'], color = 'green')
plt.plot(valido['Predictions'], color = 'red')
plt.legend(['Histórico', 'Valor real', 'Predição'])
plt.show()
#
