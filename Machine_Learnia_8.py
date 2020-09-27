# -*- coding: utf-8 -*-
"""
Created on Fri May 29 00:51:58 2020

@author: nicol
"""

### Machine learnia vidéo 16

import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import interp1d
from scipy import optimize

"""
x = np.linspace(0, 2, 100)
y = 1/3*x**3 - 3/5*x**2 + 2 + np.random.randn(x.shape[0])/20
plt.scatter(x, y)

def f(x, a, b, c, d):
    return(a*x**3 + b*x**2 + c*x + d)


params, param_cov = optimize.curve_fit(f, x, y)

plt.scatter(x, y)
plt.plot(x, f(x, params[0], params[1], params[2], params[3]), c = 'g')
"""
"""
def f2(x):
    return(x**2 + 15*np.sin(x))

x = np.linspace(-10, 10, 100)

x0 = - 5
result = optimize.minimize(f2, x0 = x0).x

plt.plot(x, f2(x), lw = 3, zorder = -1)
plt.scatter(result, f2(result), s = 100, c = 'r', zorder = 1)
plt.scatter(x0, f2(x0), s = 200, marker = '+', c = 'g', zorder = 1)
plt.show()
"""
"""
x = np.linspace(0, 20, 100)
y = x + 4*np.sin(x) + np.random.randn(x.shape[0])
"""

from scipy import signal 
"""
new_y = signal.detrend(y)

plt.figure()
plt.plot(x, y)
plt.plot(x, new_y)
plt.show()
"""
### Fourier
"""
x = np.linspace(0, 30, 1000)
y = 3*np.sin(x) + 2*np.sin(5*x) + np.sin(10*x)


from scipy import fftpack
 
fourier = fftpack.fft(y)
power = np.abs(fourier)
frequences = fftpack.fftfreq(y.size)
plt.plot(np.abs(frequences), power)

"""
### filtrage
"""
x = np.linspace(0, 30, 1000)
y = 3*np.sin(x) + 2*np.sin(5*x) + np.sin(10*x) + np.random.random(x.shape[0])*10
plt.figure()
plt.plot(x, y)


from scipy import fftpack
 
fourier = fftpack.fft(y)
power = np.abs(fourier)
frequences = fftpack.fftfreq(y.size)
plt.figure()
plt.plot(np.abs(frequences), power)

fourier[power<400] = 0
plt.figure()
plt.plot(np.abs(frequences), np.abs(fourier))

filtered_signal = fftpack.ifft(fourier)
plt.figure()
plt.plot(x, y, lw = 0.5)
plt.plot(x, filtered_signal, lw = 3)
plt.show()
"""
### Morphology

from scipy import ndimage
"""
np.random.seed(0)

X = np.zeros((32, 32))
X[10:-10, 10:-10] = 1
X[np.random.randint(0, 32, 30), np.random.randint(0, 32, 30)] = 1
plt.figure()
plt.imshow(X)

open_x = ndimage.binary_opening(X)
plt.figure()
plt.imshow(open_x)
"""
### Image

image = plt.imread('bacteria.jpg')
s = image.shape
d = 8
image = image[s[0]//d:-s[0]//d, s[1]//d:-s[1]//d, 0]
plt.figure()
plt.imshow(image, cmap  = 'gray')
plt.colorbar()
plt.imshow(image)

image_2 = np.copy(image)
plt.figure()
plt.hist(image_2.ravel(), bins = 255)
plt.show()


image = image < 130
plt.figure()
plt.imshow(image)

open_x = ndimage.binary_opening(image)
plt.figure()
plt.imshow(open_x)

label_image, n_labels = ndimage.label(open_x)
plt.figure()
plt.imshow(label_image)

sizes = ndimage.sum(open_x, label_image, range(n_labels))
plt.figure()
#tailles des différentes bactéries
plt.scatter(range(n_labels), sizes, c = 'orange')
