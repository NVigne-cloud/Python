# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 23:54:44 2020

@author: nicol
"""

# =============================================================================
# Régression Linéaire Multiple et Polynomiale Numpy
# =============================================================================

import numpy as np
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

### 1 - Régression polynomiale : 1 variable x1
### 1.1 - Dataset

np.random.seed(0) # permet de reproduire l'aléatoire

x, y = make_regression(n_samples=100, n_features=1, noise = 10) # creation d'un dataset (x, y) linéaire
y = y + abs(y/2) # modifie les valeurs de y pour rendre le dataset non-linéaire

plt.figure(0)
plt.scatter(x, y) # afficher les résultats. x en abscisse et y en ordonnée

# Verification des dimensions
print(x.shape)
print(y.shape)

# redimensionner y
y = y.reshape(y.shape[0], 1)
print(y.shape)

# Création de la matrice X, inclut le Biais
X = np.hstack((x, np.ones(x.shape)))
X = np.hstack((x**2, X)) # ajoute le vecteur x^2 a la gauche de la matrice X

print(X.shape)
print(X[:10])

# Initialisation du vecteur theta aléatoire, avec 3 éléments (car X a trois colonnes)
theta = np.random.randn(3, 1)
theta

### 1.2 - Modèle linéaire

def model(X, theta):
    return X.dot(theta)

plt.figure(1)
plt.scatter(x, y)
plt.scatter(x, model(X, theta), c='r')

### 1.3 - Fonction Cout : Erreur Quadratique moyenne

def cost_function(X, y, theta):
    m = len(y)
    return 1/(2*m) * np.sum((model(X, theta) - y)**2)

### 1.4 - Gradients et Descente de Gradient

def grad(X, y, theta):
    m = len(y)
    return 1/m * X.T.dot(model(X, theta) - y)

def gradient_descent(X, y, theta, learning_rate, n_iterations):    
    cost_history = np.zeros(n_iterations) # création d'un tableau de stockage pour enregistrer l'évolution du Cout du modele
    for i in range(0, n_iterations):
        theta = theta - learning_rate * grad(X, y, theta) # mise a jour du parametre theta (formule du gradient descent)
        cost_history[i] = cost_function(X, y, theta) # on enregistre la valeur du Cout au tour i dans cost_history[i]
    return theta, cost_history

### 1.5 - Phase d'entraînement

n_iterations = 1000
learning_rate = 0.01

theta_final, cost_history = gradient_descent(X, y, theta, learning_rate, n_iterations)

print(theta_final)

# création d'un vecteur prédictions qui contient les prédictions de notre modele final
predictions = model(X, theta_final)

# Affiche les résultats de prédictions (en rouge) par rapport a notre Dataset (en bleu)
plt.figure(2)
plt.scatter(x, y)
plt.scatter(x, predictions, c='r')

### 1.6 - Courbes d'apprentissage

plt.figure(3)
plt.plot(range(n_iterations), cost_history)

### 1.7 - Évaluation finale

def coef_determination(y, pred):
    u = ((y - pred)**2).sum()
    v = ((y - y.mean())**2).sum()
    return 1 - u/v

print(coef_determination(y, predictions))

### 2 - Régression Multiples Variables

### 2.1 - Dataset

np.random.seed(0) # permet de reproduire l'aléatoire

x, y = make_regression(n_samples=100, n_features=2, noise = 10) # creation d'un dataset (x, y) linéaire

plt.figure(4)
plt.scatter(x[:,0], y) # afficher les résultats. x_1 en abscisse et y en ordonnée

from mpl_toolkits.mplot3d import Axes3D
#%matplotlib notebook #activez cette ligne pour manipuler le graph 3D

fig = plt.figure(5)
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x[:,0], x[:,1], y) # affiche en 3D la variable x_1, x_2, et la target y

# affiche les noms des axes
ax.set_xlabel('x_1')
ax.set_ylabel('x_2')
ax.set_zlabel('y')

# Verification des dimensions
print(x.shape)
print(y.shape)

# redimensionner y
y = y.reshape(y.shape[0], 1)
print(y.shape)

# Création de la matrice X, inclut le Biais
X = np.hstack((x, np.ones((x.shape[0], 1)))) # ajoute un vecteur Biais de dimension (x.shape[0], 1)

print(X.shape)
print(X[:10])

# Initialisation du vecteur theta aléatoire, avec 3 éléments (car X a trois colonnes)
theta = np.random.randn(3, 1)
print(theta)

### 2.5 - Phase d'entraînement 

n_iterations = 1000
learning_rate = 0.01

theta_final, cost_history = gradient_descent(X, y, theta, learning_rate, n_iterations)

# création d'un vecteur prédictions qui contient les prédictions de notre modele final
predictions = model(X, theta_final)

print(theta_final)

fig = plt.figure(6)
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x[:,0], x[:,1], y)
ax.scatter(x[:,0], x[:,1], predictions)

plt.figure(7)
plt.plot(range(n_iterations), cost_history)

print(coef_determination(y, predictions))