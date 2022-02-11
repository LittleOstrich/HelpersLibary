import os

from helpers.fileTools import copyFiles, isCsv

base = "C:\\Users\\geiss\\OneDrive\\Desktop"
src = base + os.sep + "AramisData"
dst = base + os.sep + "AramisDataTmp\\AramisData"

f = lambda x: x.endswith(".h5")
f2 = lambda x: f(x) or isCsv(x)
copyFiles(src, dst, f2)
