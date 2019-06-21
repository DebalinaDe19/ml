import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

diabetes = pd.read_csv('diabetes_data.csv')
print(diabetes.head())
