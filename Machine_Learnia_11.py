# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:45:02 2020

@author: nicol
"""


###Vidéo 19

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
"""
iris = pd.read_csv('iris.csv')

plt.figure()
sns.pairplot(iris, hue = 'species')

#sns.fonction(x, y, data, hue, size, style)
"""
titanic = sns.load_dataset('titanic')


print(titanic.head())

titanic.drop(['alone', 'alive', 'who', 'adult_male', 'embark_town', 'class'], axis = 1, inplace =True)
titanic.dropna(axis = 0, inplace = True)
print(titanic.head())

plt.figure()
# sns.pairplot(titanic)
plt.figure()
sns.catplot(x = 'pclass', y ='age', data = titanic, hue = 'sex')
plt.figure()
sns.boxplot(x = 'pclass', y ='age', data = titanic, hue = 'sex')
plt.figure()
sns.distplot(titanic['fare'])
plt.figure()
sns.jointplot('age', 'fare', data = titanic, kind ='hex')
plt.figure()
sns.heatmap(titanic.corr())
