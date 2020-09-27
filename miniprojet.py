# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:56:50 2020

@author: nicol
"""


import numpy as np
import matplotlib.pyplot as plt
import csv
"""
E = np.zeros((8,8))
E[0,7] = 1
I = np.eye(8)
X = I + E
y = np.ones((8,1))
XT = np.transpose(X)
D = np.dot(XT,X)
B = np.linalg.inv(D)
B = np.dot(B,XT)
B = np.dot(B,y)


Q2 = D-I
VP = np.linalg.eigvals(Q2)

print(VP)
"""

import numpy as np
data = np.loadtxt('2.csv', delimiter=';')
Z = data[:,0:11]
y = data[:,11]
ZT = np.transpose(Z)        
D = np.dot(ZT,Z)
B = np.linalg.inv(D)
B = np.dot(B,ZT)
B = np.dot(B,y)

résidu = np.dot(Z,B)-y
résidu = np.linalg.norm(résidu,2)**2

X = Z
i = 0

for i in range(11):
    X[:,i] = (Z[:,i]-np.mean(Z[:,i]))/np.std(Z[:,i])
    
XT = np.transpose(X)
D = np.dot(XT,X)
B = np.linalg.inv(D)
B = np.dot(B,XT)
B = np.dot(B,y)
résidu = np.dot(Z,B)-y
résidu = np.linalg.norm(résidu,2)**2