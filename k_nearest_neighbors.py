import mglearn
#The iris dataset
from sklearn.datasets import load_iris
iris_dataset = load_iris()
print("keys of iris_dataset: \n{}".format(iris_dataset.keys()))
#The Boston Housing dataset (A real-world regression dataset)
from sklearn.datasets import load_boston
boston = load_boston()
print("Data shape: {}".format(boston.data.shape))
#Result: Data shape: (506, 13)
#Meaning: 506 data points described by 13 features
print(boston['DESCR'][:193]+"\n...")
#feature engineering: Add interactions (products) between features
X,y = mglearn.datasets.load_extended_boston()
print("X.shape: {}".format(X.shape))
#Result: X.shape: (506, 104)
#104 = 13 + 13°5 (puissance: toutes les combinaisons possibles)
#k-Neighbors classification
mglearn.plots.plot_knn_classification(n_neighbors=1)
