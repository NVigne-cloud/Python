# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:56:30 2020

@author: nicol
"""


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
x = np.linspace(0, 2, 10)
y = x**2
"""
plt.figure()
plt.plot(x,y, c = 'red', label = 'quadratique')
plt.plot(x, x**3, label = 'cubique')
plt.title('figure 1')
plt.xlabel('axe x')
plt.ylabel('axe y')
#plt.scatter(x,y, c = 'red')
plt.legend()
plt.grid()
plt.show()
#plt.savefig('text.png)

#plt.subplot(2, 1, 1)
"""
fig, ax = plt.subplots(2, 1, sharex = True)
ax[0].plot(x, y)
ax[1].plot(x, np.sin(x))
plt.show()
np.random.seed(0)
dataset = {f"experience{i}" : np.random.randn(100) for i in range(6)}

def graphique(dataset):
    n = len(dataset)
    fig, ax = plt.subplots(n, 1, sharex = True)
    for i in range(n):
        ax[i].plot(dataset[f"experience{i}"])
    plt.show


graphique(dataset)

x = iris.data
y = iris.target
names = list(iris.target_names)

def graphique_2(iris):
    n = x.shape[1]
    for i in range(n):
        plt.subplot(n//2, n//2, i+1)
        plt.scatter(x[:,0], x[:,i], c = y)
        plt.xlabel('0')
        plt.ylabel(i)
    plt.show
    
graphique_2(iris)