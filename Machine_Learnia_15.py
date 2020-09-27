# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 14:05:18 2020

@author: nicol
"""


### Vidéo 23

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

### 1 - Variance Threshold

from sklearn.feature_selection import VarianceThreshold

from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

plt.figure()
plt.plot(X)
plt.legend(iris.feature_names)

X.var(axis=0)

selector = VarianceThreshold(threshold=0.2)
selector.fit(X)

selector.get_support()

np.array(iris.feature_names)[selector.get_support()]

selector.variances_

### 2 - SelectKBest

from sklearn.feature_selection import SelectKBest, chi2, f_classif

chi2(X, y)

selector = SelectKBest(f_classif, k=2)
selector.fit(X, y)
selector.scores_

print(np.array(iris.feature_names)[selector.get_support()])

### 3 - Recursive feature Elimination

from sklearn.feature_selection import RFECV
from sklearn.linear_model import SGDClassifier

selector = RFECV(SGDClassifier(random_state=0), step=1, min_features_to_select=2, cv=5)
selector.fit(X, y)
print(selector.ranking_)
print(selector.grid_scores_)

print(np.array(iris.feature_names)[selector.get_support()])

### 4 - SelectFromModel

from sklearn.feature_selection import SelectFromModel

X = iris.data
y = iris.target
selector = SelectFromModel(SGDClassifier(random_state=0), threshold='mean')
selector.fit(X, y)
print(selector.estimator_.coef_)

print(np.array(iris.feature_names)[selector.get_support()])