import numpy as np

from helpers.numpyTools import matrixToFile, invIndexSlicing


#
# A = np.arange(100).reshape((10, 10))
# dstDir = "tmp"
# fn = "dump.txt"
# matrixToFile(A, dstDir, fn)



def invIndexSlicingTests():

    A = np.arange(10)
    b = np.array([1,6,3,7])

    ret = invIndexSlicing(A, b)
    print(ret)


invIndexSlicingTests()