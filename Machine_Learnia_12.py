# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:37:47 2020

@author: nicol
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

np.random.seed(0)

m = 100
X = np.linspace(0, 10, m).reshape(m, 1)
y = X + np.random.randn(m, 1)

plt.figure()
plt.scatter(X, y)

from sklearn.linear_model import LinearRegression

### forme typique de code

model = LinearRegression()
model.fit(X, y)
print(model.score(X, y))
predictions = model.predict(X)
plt.plot(X, predictions, c = "r")

from sklearn.svm import SVR

y = X**2 + np.random.randn(m, 1)

model = SVR(C=100)
model.fit(X, y)
model.score(X,y)

predictions = model.predict(X)
plt.figure()
plt.scatter(X, y)
plt.plot(X, predictions, c='r', lw = 3)

titanic = sns.load_dataset('titanic')

titanic = titanic[['survived', 'pclass', 'sex', 'age']]
titanic.dropna(axis = 0, inplace = True)
titanic['sex'].replace(['male', 'female'], [0, 1], inplace = True)

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()

y = titanic['survived']
X = titanic.drop('survived', axis = 1)
y = y.ravel()
y = y.reshape(y.shape[0], 1)
model.fit(X, y)
print(model.score(X, y)) #accuracy

def survie(model, pclass, sex, age):
    x = np.array([pclass, sex, age]).reshape(1, 3)
    print(model.predict(x))
    print(model.predict_proba(x))
    
### Correction exercice (attention ce n'est pas une bonne idée d'optimisation)
"""
score =[]

best_k = 1

best_score = 0

for k in range(best_k,30):
    model = KNeighborsClassifier(n_neighbors = k)
    model.fit(X, y)
    score.append(model.score(X, y))
    if best_score < model.score(X, y):
        best_k = k
        best_score = model.score(X,y)
        
print(best_k)
plt.figure()
plt.plot(score)
"""