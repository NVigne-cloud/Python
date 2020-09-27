# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:14:48 2020

@author: nicol
"""


### Vidéo 22


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y, alpha=0.8)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold, LeaveOneOut, ShuffleSplit, StratifiedKFold, GroupKFold, GroupShuffleSplit

#cv = KFold(5, random_state = 0)
#cv = LeaveOneOut()
# cv = ShuffleSplit(4, test_size = 0.2)
#cv = StratifiedKFold(4)
cv = GroupKFold(5).get_n_splits(X, y, groups = X[:, 0])
print(cross_val_score(KNeighborsClassifier(), X, y, cv = cv))

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import *

y = np.array([1, 2, 2, 3, 5, 2])
y_pred = np.array([5, 2, 2, 5, 7, 1000])

print('MAE :', mean_absolute_error(y, y_pred))
print('RMSE :', np.sqrt(mean_squared_error(y, y_pred)))
print('median absolute error :', median_absolute_error(y, y_pred))

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

boston = load_boston()
X = boston.data
y = boston.target

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

plt.figure()
plt.scatter(X[:, 5], y, label = 'y')
plt.scatter(X[:, 5], y_pred, alpha = 0.8, label = 'y_pred')
plt.legend()

plt.figure()
err_hist = np.abs(y - y_pred)
plt.hist(err_hist, bins = 50)
plt.show()

print(model.score(X, y))

print(cross_val_score(LinearRegression(), X, y, cv = 3, scoring = 'neg_mean_absolute_error'))


import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, LabelBinarizer, OrdinalEncoder, OneHotEncoder

### 1 - Encodage

y = np.array(['Chat',
              'Chien',
              'Chat',
              'Oiseau'])

encoder = LabelEncoder()
print(encoder.fit_transform(y))

print(encoder.inverse_transform(np.array([0, 0, 2])))

encoder = LabelBinarizer()
print(encoder.fit_transform(y))

X = np.array([['chat', 'poils'],
              ['chien', 'poils'],
              ['chat', 'poils'],
              ['oiseau', 'plumes']])

encoder = OrdinalEncoder()
print(encoder.fit_transform(X))

encoder = OneHotEncoder(sparse=False)
print(encoder.fit_transform(X))

### 2 - Normalisation

from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data

### MinMaxScaler

X_minmax = MinMaxScaler().fit_transform(X)

plt.figure()
plt.scatter(X[:, 2], X[:, 3])
plt.scatter(X_minmax[:, 2], X_minmax[:, 3])

### StandardScaler

X_stdscl = StandardScaler().fit_transform(X)

plt.figure()
plt.scatter(X[:, 2], X[:, 3])
plt.scatter(X_stdscl[:, 2], X_stdscl[:, 3])

### RobustScaler 

X_robust = RobustScaler().fit_transform(X)

plt.figure()
plt.scatter(X[:, 2], X[:, 3])
plt.scatter(X_robust[:, 2], X_robust[:, 3])

### 3 - Polynomial Features

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

m = 100
X = np.linspace(0, 4, m).reshape((m, 1))
y = X**2 + 5*np.cos(X) + np.random.randn(m, 1)

model = LinearRegression().fit(X, y)
y_pred = model.predict(X)

plt.figure()
plt.scatter(X, y)
plt.plot(X, y_pred, c='r', lw=3)

X_poly = PolynomialFeatures(3).fit_transform(X)
model = LinearRegression().fit(X_poly, y)
y_pred = model.predict(X_poly)

plt.figure()
plt.scatter(X, y)
plt.plot(X, y_pred, c='r', lw=3)

### 4 - Discretisation

from sklearn.preprocessing import Binarizer, KBinsDiscretizer

X = np.linspace(0, 5, 10).reshape((10, 1))

print(np.hstack((X, Binarizer(threshold=3).fit_transform(X))))
print(KBinsDiscretizer(n_bins=6).fit_transform(X).toarray())

### 5 - Pipelines

from sklearn.pipeline import make_pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

model = make_pipeline(StandardScaler(), SGDClassifier())

model.fit(X_train, y_train)
print(model.score(X_test, y_test))

from sklearn.model_selection import GridSearchCV

model = make_pipeline(PolynomialFeatures(),
                      StandardScaler(),
                      SGDClassifier(random_state=0))
params = {
    'polynomialfeatures__degree':[2, 3, 4],
    'sgdclassifier__penalty':['l1', 'l2']
}

grid = GridSearchCV(model, param_grid=params, cv=4)

print(grid.fit(X_train, y_train))

print(grid.score(X_test, y_test))