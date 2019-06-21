
#importing packages and libraries
import numpy as np
import pandas as pd
          
dataset = pd.read_csv('diabetes_data.csv')

dataset.describe()


dataset.groupby('diabetes').size()
           
feature_column=['pregnancies','glucose','diastolic','triceps','insulin','bmi','dpf','age','diabetes']

X=dataset[feature_column].values

y=dataset['diabetes'].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)


import matplotlib.pyplot as plt
import sklearn.datasets as dataset
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier


mlp=MLPClassifier(hidden_layer_sizes=(100), max_iter=150,alpha=1e-4,
                  solver='sgd',verbose=10, tol=1e-4,random_state=1,
                  learning_rate_init=.01)
mlp.fit(X_train, y_train)
y_pred=mlp.predict(X_test)

mlp.fit(X_test, y_test)
accuracy=accuracy_score(y_test,y_pred)*100
print('Accuracy of our model is equal to:'+str(round(accuracy,1))+'%')
