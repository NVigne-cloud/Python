# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 00:13:37 2020

@author: nicol
"""
# =============================================================================
# Machine Learnia vidéo 17
# =============================================================================

###Machine Learnia vidéo 17

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('titanic3.xls')

dimensions = data.shape

colonnes =  data.columns
en_tête = data.head()

### partie 1

data = data.drop(['name', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'], axis = 1)

print(data.head())

description = data.describe()

# on pourrait utiliser data.fillna([]) mais cela corromprait le fichier
data = data.dropna(axis = 0)

description = data.describe()

classes = data['pclass'].value_counts()

plt.figure()
data['pclass'].value_counts().plot.bar()

plt.figure()
data['age'].hist()
print(f"\n")
print(data.groupby(['sex']).mean())
print(f"\n")
print(data.groupby(['sex', 'pclass']).mean())

### partie 2

#
print(data['age'])
print(f'\n')
print(data['age'][0:10])
print(f'\n')
print(data['age']<18)
print(f'\n')
print(data[data['age']<18]['pclass'].value_counts())
print(f'\n')
print(data[data['age']<18].groupby(['sex', 'pclass']).mean())
print(f'\n')
print(data.iloc[0:2, 0:2])
print(f'\n')

### Exercice
"""
for i in range(len(data['age'])):
    if data['age'][i] <= 20:
        data['age'][i] = 0
    elif data['age'][i] <= 30:
        data['age'][i] = 1
    elif data['age'][i] <= 40:
        data['age'][i] = 2
    else :
        data['age'][i] = 3
"""

### Correction

data.loc[data['age'] <= 20, 'age'] = 0
data.loc[(data['age'] > 20) & (data['age'] <= 30), 'age'] = 1
data.loc[(data['age'] > 30) & (data['age'] <= 40), 'age'] = 2
data.loc[data['age'] > 40, 'age'] = 3

print(data.groupby(['age']).mean())

### Fonction map()

print(data['age'].map(lambda x:x+1))

def category_ages(age):
    if age <= 20:
        return '<20 ans'
    elif (age > 20) & (age <= 30):
        return '20-30 ans'
    elif (age > 30) & (age <= 40):
        return '30-40 ans'
    else:
        return '+40 ans'

print(data["age"].map(category_ages))

print(data['sex'].map({'male':0, 'female':1}))

print(data['sex'].replace(['male', 'female'], [0, 1]))

print(data['sex'].astype('category').cat.codes)