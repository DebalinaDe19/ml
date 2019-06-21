import pandas as pd
url='http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

col_names=['Sepal-length','Petal-length','Sepal-width','Petal-width','species']

iris = pd.read_csv(url, header=None, names=col_names)

iris_class = {'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2}
iris['species_num'] = [iris_class[i] for i in iris.species]

X = iris.drop(['species', 'species_num'], axis=1)
y = iris.species_num

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)
print(knn.score(X_test, y_test))
