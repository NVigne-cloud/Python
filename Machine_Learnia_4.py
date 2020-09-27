# -*- coding: utf-8 -*-
"""
Created on Mon May 25 23:13:23 2020

@author: nicolas
"""


import numpy as np

"""
A = np.random.randint(0, 10, [5, 5])

print(A.sum(axis = 0))

print(A.sum(axis = 1))

print(A.cumsum())

print(A.cumprod())

print(A.argmin(axis = 0))

print(A.argmin(axis = 1))

print(A.argsort(axis = 1))

C = np.exp(A)

D = np.sinh(A)

print(A.mean(axis = 0))

print(A.var(axis = 0))

print(A.std(axis = 0))

E = np.corrcoef(A)

e = np.corrcoef(A)[0, 1]

print(f'\n')

values, counts = np.unique(A, return_counts = True)



for i, j in zip(values[counts.argsort()], counts[counts.argsort()]) :
    print(f'la valeur {i} apparait {j} fois')
    
A = np.random.randn(5, 5)
A[0, 2] = np.nan
A[4, 3] = np.nan

print(np.nanmean(A))
print(np.nanstd(A))

F = np.isnan(A)
f = F.sum()
f_2 = np.isnan(A).sum()/A.size

G = A
G[F] = 0

A = np.ones((2, 3))
B = np.ones((3, 2))

C = A.T

D = A.dot(B)
E = B.dot(A)

A = np.random.randint(0, 10, [5, 5])
a = np.linalg.det(A)
B = np.linalg.inv(A)

a = np.linalg.eig(A)

"""

### Exercice

np.random.seed(0)
A = np.random.randint(0, 100, [10, 5])
A = A.astype(float)
for i in range(np.size(A, axis = 1)):
    A[:,i] = (A[:,i] - np.mean(A[:,i]))/np.std(A[:,i])
    
### Correction

np.random.seed(0)
A = np.random.randint(0, 100, [10, 5])
A = (A - A.mean(axis = 0))/A.std(axis = 0)

print(f'\nMoyenne de chaque colonne : \n{A.mean(axis = 0)} \nÉcart-type de chaque colonne : \n{A.std(axis = 0)} ')