# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:28:18 2020

@author: nicol
"""

### BROADCASTING

import numpy as np

np.random.seed(0)

A = np.random.randint(0, 10 ,[4, 1])

B = np.ones((1, 3))

C = A + B

from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

x, y = make_regression(n_samples = 100, n_features = 1, noise = 10)

y = y.reshape(y.shape[0],1)

plt.scatter(x, y)

z = x - y

### BILAN

#attributs

A.shape()
A.size()

#constructeurs

np.array(objet, dtype)
np.zeros((shape), dtype)
np.ones((shape), dtype)
np.random.randn(lignes, colonnes)

#Manipulation

A.reshape((shape))
A.ravel()
A.concatenate(axis)

#Méthodes utiles

A.min(axis)
A.max(axis)
A.sum(axis)
A.mean(axis)
A.std(axis)

A.argmin(axis)
A.argmax(axis)
A.argsort(axis)

#Boolean indexing

A[A<10]