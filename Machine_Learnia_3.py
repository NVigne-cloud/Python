# -*- coding: utf-8 -*-
"""
Created on Sun May 24 22:13:50 2020

@author: nicol
"""


import numpy as np

A = np.array([1, 2, 3])
A = A.reshape((A.shape[0], 1))
# A = A.squeeze()
B = np.zeros((3, 2))
C = np.ones((3, 4))
D = np.full((2, 3), 9)
np.random.seed(0)
E = np.random.randn(3, 4)

t = np.linspace(0,0.9,10)
l= np.arange(0,1,0.1)

F = np.linspace(0,1,10, dtype = np.float16)

A = np.zeros((3, 2))
B = np.ones((3, 2))

C = np.hstack((A, B))
D = np.vstack((A, B))

C = np.concatenate((A, B), axis = 1)
D = np.concatenate((A, B), axis = 0)

C = C.reshape((3, 4))
D = D.reshape((3, 4))

C = C.ravel()

def initialisation(m, n):
    X = np.random.randn(m,n)
    return np.concatenate((X,np.ones((X.shape[0],1))), axis = 1) 

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = A[0:2,0:2] = 10
C = A[:,-2:]

B = np.zeros((4, 4))
B[1:3,1:3] = 2

C = np.zeros((5, 5))
C[::2,::2] = 1

A = np.random.randint(0, 10, [5, 5])
print(A)
A[(A<5) & (A>2)] = 10
print(A)
"""
A = np.random.randint(0, 255, [1024, 720])
A[A>200] = 255
"""
B = np.random.randn(5, 5)
B[A<5]

from scipy import misc
import matplotlib.pyplot as plt
face = misc.face(gray = True)
plt.imshow(face, cmap = plt.cm.gray)
plt.show

h = face.shape[0]
w = face.shape[1]
zoom_face = face[h//4 : -h//4 , w//4 : -w//4]
zoom_face[zoom_face > 200] = 200
zoom_face[zoom_face < 50] = 50
plt.imshow(zoom_face, cmap = plt.cm.gray)
plt.show