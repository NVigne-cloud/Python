# -*- coding: utf-8 -*-
"""
Created on Wed May 20 23:35:40 2020

@author: nicol
"""

import numpy as np


def e_potentielle(masse, hauteur, e_limite, g = 9.81):
    E = masse * hauteur * g
    if E >= e_limite : 
        print('Énérgie limite dépassée')
    else :
        print('Énérgie limite non atteinte')
    
def fibonacci(n):
    u0 = 0
    u1 = 1
    u = []
    u.append(u0)
    u.append(u1)
    for i in range(n-1):
        if n >= 2:
            u.append(u0+u1)
            u0 = u[-2]
            u1 = u[-1]
    return u

traduction = {
    "chien"     : "dog",
    "chat"      : "cat",
    "souris"    : "mouse",
    "oiseau"    : "bird",    
    }



dictionnaire_3 = {
    "dict_1" : traduction,
    }

parametres = {
    "W1" : np.random.randn(10,100),
    "b1" : np.random.randn(10,1),
    "W2" : np.random.randn(10,10),
    "b2" : np.random.randn(10,1),
    }

classeur = {
    "positif"   :   [],
    "négatif"   :   [],
    }

def trier(classeur, nombre):
    if nombre < 0 :
        classeur["négatif"].append(nombre)
    else :
        classeur["positif"].append(nombre)
    return classeur

liste_2 = [i**2 for i in range(10)]

liste_3 = [[i for i in range(3)] for j in range(3)]

prenoms = ['Pierre', 'Jean', 'Julie', 'Sophie']

dico = {k:v for k,v in enumerate(prenoms)}


ages = [24, 62, 10, 23]

dico_2 = {prenom:age for prenom,age in zip(prenoms,ages) if age > 30}

tuple_1 = tuple((i**2 for i in range(10)))


dictionnaire = {k:v for k,v in enumerate(i**2 for i in range(21))}

with open('fichier.txt', 'w') as f:
    for i in range(10):
        f.write("{}^2 = {} \n".format(i, i**2))
        
with open("fichier.txt") as f:
    liste = f.read().splitlines()
    
liste = [line.strip() for line in open('fichier.txt', 'r')]
    