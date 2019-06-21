import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

diabetes = pd.read_csv('diabetes_data.csv')
print(diabetes.head())
feature_column=['pregnancies','glucose','diastolic','triceps','insulin','bmi','dpf','age','diabetes']

X=diabetes[feature_column].values

y=diabetes['diabetes'].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)



diabetesCheck = LogisticRegression(solver='lbfgs')
diabetesCheck.fit(X_train, y_train)


accuracy = diabetesCheck.score(X_test, y_test)
print("accuracy = ", accuracy * 100, "%")
