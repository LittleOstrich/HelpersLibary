import os

import shutil

# "E:\\AramisData",

from helpers.folderTools import recursiveWalk
from helpers.timeTools import myTimer


def writeLines(fn, dstDir, lines):
    ffp = dstDir + os.sep + fn
    f = open(ffp, "w+")
    for line in lines:
        f.write(line)
    f.close()


def getParentDirs(baseDirs, dstDirs):
    mt = myTimer("copyParentDirs")

    N = len(baseDirs)
    for i in range(N):
        mt.start()
        bd = baseDirs[i]
        dstDir = dstDirs[i]
        ds, _ = recursiveWalk(bd)
        print(ds)
        for d in ds:
            files = os.listdir(d)
            hasCSVFiles = False
            destParentDir = None

            for f in files:
                if f.endswith(".csv"):
                    hasCSVFiles = True
                    subdir = d.split(os.sep)[-1]
                    destParentDir = dstDir + os.sep + subdir
                    os.makedirs(destParentDir, exist_ok=True)
                    break
            if hasCSVFiles:
                for f in files:
                    if f.endswith(".csv"):
                        fullDestPath = destParentDir + os.sep + f
                        c = c + 1
                        shutil.copy(d + os.sep + f, fullDestPath)
                        if c % 1000 == 0:
                            print(c)
    mt.end()


def remove_files(files):
    for file in files:
        if os.path.isfile(file):
            os.remove(file)


def isCsv(s: str):
    ret = s.endswith(".csv")
    return ret


def copyFiles(src, dst, filter=lambda x: True, debug=False):
    _, fs = recursiveWalk(src, filterFunction=filter)
    N = len(fs)
    for i in range(N):
        f = fs[i]
        isOk = filter(f)
        if isOk:
            tail = f.replace(src, "")
            newDst = dst + tail
            shutil.copy(f, newDst)
            if debug:
                print("src: ", src)
                print("dst: ", newDst)
# baseDirs = [
#     # "H:",
#     "G:"
#     "F:",
# ]
# # "E:\\AramisData\\LME LFT",
# destDirs = [
#     # "E:\\AramisData\\LME1",
#     "E:\\AramisData\\LME2", "E:\\AramisData\\LME3"
# ]
# H = ""
# func = lambda x: x.endswith(".csv")
# N = len(H)
# c = 0
# mt = myTimer("copyingTask")
