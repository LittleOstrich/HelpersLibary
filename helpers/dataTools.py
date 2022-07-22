import numpy as np
from sklearn import datasets
from sklearn.datasets import make_classification, make_gaussian_quantiles
from sklearn.model_selection import train_test_split


def dummyGaussian(mean=[0, 0], cov=[[1, 0], [0, 100]], N=100):
    x = np.random.multivariate_normal(mean, cov, N)
    y = np.random.choice([0, 1], N)
    return x, y


def multiCollinearityData():
    x1 = np.random.random((100, 1))
    x2 = x1 * 2 + 1
    x = np.concatenate([x1, x2], axis=1)
    y = 3 * x1 + 4 * x2 - 1
    return x, y


def dummyVariableTrap():
    N = 100
    x1 = np.random.random((N, 1))
    x2 = np.random.choice([0, 1], N).reshape((N, 1))
    x3 = np.ones_like(x2) - x2
    y = x1 + 2 * x2 + x3 + 1
    x = np.concatenate([x1, x2, x3], axis=1)
    return x, y


def dummyVariableTrap2():
    N = 100

    x1 = np.random.choice([0, 1], N).reshape((N, 1))
    x2 = np.ones_like(x1) - x1

    y = 2 * x1 + 4 * x2 + 1
    x = np.concatenate([x1, x2], axis=1)
    return x, y


def irisData():
    iris = datasets.load_iris()
    x = iris.data[:, :2]
    y = iris.target
    return x, y


def makeClassification(n_features=2, n_redundant=0,
                       n_informative=1, n_clusters_per_class=1):
    x, y = make_classification(
        n_features=n_features, n_redundant=n_redundant,
        n_informative=n_informative, n_clusters_per_class=n_clusters_per_class
    )
    return x, y


def gaussianQuantiles(n_samples=100, n_features=2, n_classes=3):
    x, y = make_gaussian_quantiles(n_samples=n_samples, n_features=n_features, n_classes=n_classes)
    return x, y


def trainTestSplit(X, y, test_size=0.25):
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    return x_train, x_test, y_train, y_test
