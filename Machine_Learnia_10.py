# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:10:07 2020

@author: nicol
"""


### Vidéo 18

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

bitcoin = pd.read_csv('BTC-EUR.csv', index_col = 'Date', parse_dates = True)

plt.figure()
bitcoin['Close'].plot()
plt.show()

plt.figure()
bitcoin['2017':'2019']['Close'].plot()
plt.show()

# pd.to_datetime('2019/03/20')

plt.figure()
bitcoin.loc['2019','Close'].resample('M').plot()
plt.show()

plt.figure()
bitcoin.loc['2019','Close'].resample('2W').mean().plot()
plt.show()

plt.figure()
bitcoin.loc['2019','Close'].resample('2W').std().plot()
plt.show()

plt.figure()
bitcoin.loc['2019','Close'].plot()
bitcoin.loc['2019','Close'].resample('M').mean().plot(label = 'moyenne par mois', lw = 3, ls = ':', alpha = 0.8)
bitcoin.loc['2019','Close'].resample('W').mean().plot(label = 'moyenne par semaine', lw = 3, ls = '--', alpha = 0.8)
plt.legend()
plt.show()

m = bitcoin.loc['2019', 'Close'].resample('W').agg(['mean', 'std', 'min', 'max'])

plt.figure()
m['mean']['2019'].plot(label = 'moyenne par semaine')
plt.fill_between(m.index, m['max'], m['min'], alpha = 0.2, label = 'min-max par semaine')
plt.legend()
plt.show()

plt.figure()
bitcoin.loc['2019', 'Close'].rolling(window = 7).mean().plot()
plt.show()

plt.figure()
bitcoin.loc['2019-09', 'Close'].plot()
bitcoin.loc['2019-09', 'Close'].rolling(window = 7).mean().plot(label = 'moving average', lw = 3, ls = ':', alpha = 0.8)
bitcoin.loc['2019-09', 'Close'].rolling(window = 7, center = True).mean().plot(label = 'centered moving average', lw = 3, ls = ':', alpha = 0.8)
bitcoin.loc['2019-09', 'Close'].ewm(alpha = 0.6).mean().plot(label = 'ewm', lw = 3, ls = ':', alpha = 0.8)
plt.legend()
plt.show()


plt.figure()
bitcoin.loc['2019-09', 'Close'].plot()
for i in np.arange(0.2, 1, 0.2):
    bitcoin.loc['2019-09', 'Close'].ewm(alpha = i).mean().plot(label = f'ewm {i}', lw = 1, ls = '--', alpha = 0.8)
plt.legend()
plt.show()

ethereum = pd.read_csv('ETH-EUR.csv', index_col = 'Date', parse_dates = True)

btc_eth = pd.merge(bitcoin, ethereum, on = 'Date', how = 'inner', suffixes = ('_btc', '_eth'))
# fusion_2 = pd.merge(bitcoin, ethereum, on = 'Date', how = 'outer', suffixes = ('_btc', '_eth'))

plt.figure()
btc_eth[['Close_btc', 'Close_eth']].plot(subplots = True)
plt.show()


print(btc_eth[['Close_btc', 'Close_eth']].corr())

### Exercice

data = bitcoin.copy()
data['Buy'] = np.zeros(len(data))
data['Sell'] = np.zeros(len(data))

data['RollingMax'] = data['Close'].shift(1).rolling(window = 28).max()  #shift(1) est un décallage d'un jour
data['RollingMin'] = data['Close'].shift(1).rolling(window = 28).min()
data.loc[data['RollingMax'] < data['Close'], 'Buy'] = 1
data.loc[data['RollingMin'] > data['Close'], 'Sell'] = -1

start = '2019'
end = '2019'

fig, ax = plt.subplots(2, sharex = True)
ax[0].plot(data['Close'][start:end])
ax[0].plot(data['RollingMin'][start:end])
ax[0].plot(data['RollingMax'][start:end])
ax[0].legend(['Close', 'min', 'max'])
ax[1].plot(data['Buy'][start:end], c = 'g')
ax[1].plot(data['Sell'][start:end], c = 'r')
ax[1].legend(['buy', 'sell'])


