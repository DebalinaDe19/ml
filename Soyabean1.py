
import pandas as pd
url='https://archive.ics.uci.edu/ml/machine-learning-databases/soybean/soybean-small.data'

col_names=['species_num','date','plant-stand','precip','temp',' hail','crop-hist',
           'area-damaged','severity','seed-tmt','germination','plant-growth'
           'leaves','leafspots-halo','leafspots-marg','leafspots-marg',
           'leafspot-size','leaf-shread','leaf-malf','leaf-mild','stem',
           'lodging','stem-cankers','canker-lesion','fruiting-bodies',
           'external decay','mycelium','int-discolor','sclerotia','fruit-pods'
           'fruit spots','seed','mold-growth','seed-discolor','seed-discolor',
           'shriveling','roots','species']


          
soybean = pd.read_csv(url, header=None, names=col_names)



X = soybean.drop(['species','species_num' ], axis=1)
y = soybean.species_num


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

import matplotlib.pyplot as plt
import sklearn.datasets as soybean
from sklearn.neural_network import MLPClassifier

mlp=MLPClassifier(hidden_layer_sizes=(25,3), max_iter=150,alpha=1e-4,
                  solver='sgd',verbose=10, tol=1e-4,random_state=1,
                  learning_rate_init=.1)
mlp.fit(X_train, y_train)


print("Training data score is %f", mlp.score(X_train,y_train))
print("Testing data score is %f", mlp.score(X_test, y_test))



