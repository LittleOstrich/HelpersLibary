import os

from helpers.fileTools import copyFiles


def allowedFileEndingsTest1():
    allowedFileEndings = (".h5", ".csv", ".xls")

    test1 = "jhfejrhrhj.h5"
    test2 = "jhfejrhrhj.csv"
    test3 = "jhfejrhrhj.xls"

    f = lambda x: x.endswith(allowedFileEndings)

    print(f(test1))
    print(f(test2))
    print(f(test3))


base = "C:\\Users\\geiss\\OneDrive\\Desktop"
src = base + os.sep + "AramisData"
dst = base + os.sep + "AramisDataTmp\\AramisData"

allowedFileEndings = (".h5", ".csv", ".xls")
f = lambda x: x.endswith(allowedFileEndings)
copyFiles(src, dst, f)
