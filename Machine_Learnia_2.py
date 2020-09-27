# -*- coding: utf-8 -*-
"""
Created on Sun May 24 21:30:25 2020

@author: nicol
"""


from Machine_Learnia import fibonacci

liste = fibonacci(9)

import math
import random
import statistics
import os
import glob

##########
#MATH
##########

print(math.pi)

##########
#Statistics
##########

print(statistics.mean(liste))
print(statistics.variance(liste))

##########
#random
##########

#random.seed(0)

print(random.choice(liste))
print(random.random())
print(random.randint(5,10))
print(random.randrange(100))
print(random.sample(range(100),random.randrange(10)))

random.shuffle(liste)

##########
#OS
##########

print(os.getcwd())

##########
#glob
##########

filenames = glob.glob("*.txt")
d = {}

for file in filenames:
    with open(file, 'r') as f:
        print(f.read())

for file in filenames:
    with open(file, 'r') as f:
        d[file] = f.read().splitlines()
        
print(d)
        
   
import numpy as np 

tableau = np.array([1, 2, 3])


        