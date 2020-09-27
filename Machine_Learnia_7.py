# -*- coding: utf-8 -*-
"""
Created on Thu May 28 23:22:11 2020

@author: nicol
"""


import numpy as np 
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

x = iris.data
y = iris.target
names = list(iris.target_names)
"""
print(f"x contient {x.shape[0]} exemples et {x.shape[1]} variables")
print(f"il y a {np.unique(y).size} classes")

plt.figure()
plt.scatter(x[:,0], x[:,1], c = y, alpha = 0.5, s = x[:,2]*100)
plt.xlabel('longueur sépal')
plt.ylabel('largeur sépal')
plt.show()
"""
###

from mpl_toolkits.mplot3d import Axes3D

ax = plt.axes(projection = '3d')
ax.scatter(x[:,0], x[:,1], x[:,2], c = y)

f = lambda x, y : np.sin(x) + np.cos(x + y)*np.cos(x)

X = np.linspace(0, 5 , 100)
Y = X

X, Y = np.meshgrid(X, Y)

Z = f(X, Y)

ax = plt.axes(projection = "3d")
ax.plot_surface(X, Y, Z, cmap = 'plasma')

###

plt.figure()
plt.hist(x[:,0], bins = 30)
plt.hist(x[:,1], bins = 30)

plt.figure()
plt.hist2d(x[:,0], x[:,1], cmap = 'Blues')
plt.xlabel('longueur sépal')
plt.ylabel('largeur sépal')
plt.colorbar()


from scipy import misc 
face = misc.face(gray = True)
plt.imshow(face, cmap = 'gray')
plt.figure()
plt.hist(face.ravel(),bins = 255)


###

plt.contour(X, Y, Z, 20, colors = 'black')

plt.contourf(X, Y, Z, 20, cma= 'RdGy')


###

from scipy import misc 
face = misc.face(gray = True)

# plt.imshow(face)

plt.imshow(np.corrcoef(x.T), cmap = 'Blues')
plt.colorbar()
plt.show()