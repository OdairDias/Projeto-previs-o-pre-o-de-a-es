import pandas_datareader as dados
import pandas as pd
ativo = "PETR4.SA"  # https://finance.yahoo.com/
dados_do_ativo = dados.DataReader(ativo, start="2018-01-01",end="2022-10-24", data_source='yahoo')
import matplotlib.pyplot as plt
# plt.style.use('fivethirtyeight')
# plt.style.use('default')
plt.figure(figsize=(16,8))
plt.title('Histórico de fechamento ' + ativo)
plt.plot(dados_do_ativo['Close'])
plt.xlabel('Data')
plt.ylabel('Preço de fechamento')
plt.show()