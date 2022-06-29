import numpy as np
from sklearn.model_selection import train_test_split


def dummyGaussian(mean=[0, 0], cov=[[1, 0], [0, 100]], N=100):
    x = np.random.multivariate_normal(mean, cov, N)
    y = np.random.choice([0, 1], N)
    return x, y


def trainTestSplit(X, y):
    x_train, x_test, y_train, y_test = train_test_split(X, y)
    return x_train, x_test, y_train, y_test
