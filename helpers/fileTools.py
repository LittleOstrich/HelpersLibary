import os


def writeLines(fn, dstDir, lines):
    ffp = dstDir + os.sep + fn
    f = open(ffp, "w+")
    for line in lines:
        f.write(line)
    f.close()


def recursiveWalk(sD=".", filterFuntion=None, debug=False):
    fs = set()
    ds = set()
    for root, dirs, files in os.walk(sD):
        for name in files:
            fp = os.path.join(root, name)
            if filterFuntion is None:
                fs.add(fp)
            else:
                if filterFuntion(fp):
                    fs.add(fp)
        for dir in dirs:
            dp = os.path.join(root, dir)
            if filterFuntion is None:
                ds.add(dp)
            else:
                if filterFuntion(dp):
                    ds.add(dp)
    ds = list(ds)
    fs = list(fs)
    if debug:
        for d in ds:
            print(d)
        for f in fs:
            print(f)
    return ds, fs


import os

from copyAllDataPathes import H
from helpers.fileTools import recursiveWalk
import shutil

# "E:\\AramisData",
from helpers.timeTools import myTimer

baseDirs = [
    # "H:",
    "G:"
    "F:",
]
# "E:\\AramisData\\LME LFT",
destDirs = [
    # "E:\\AramisData\\LME1",
    "E:\\AramisData\\LME2", "E:\\AramisData\\LME3"
]
func = lambda x: x.endswith(".csv")
N = len(H)
c = 0
mt = myTimer("copyingTask")


def getParentDirs():
    N = len(baseDirs)
    for i in range(N):
        mt.start()
        bd = baseDirs[i]
        destDir = destDirs[i]
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
                    destParentDir = destDir + os.sep + subdir
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


def copyParentDirs(ds):
    baseDirExits = os.path.exists(ds)
    if not baseDirExits:
        print("Base dir does not exist...")
    else:
        c = 0
        for i in range(N):
            mt.start()
            # ds = H
            destDir = destDirs[0]
            for d in ds:
                try:
                    files = os.listdir(d)
                    hasCSVFiles = False
                    destParentDir = None
                    for f in files:
                        if f.endswith(".csv"):
                            hasCSVFiles = True
                            subdir = d.split(os.sep)[-1]
                            destParentDir = destDir + os.sep + subdir
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
                except Exception as e:
                    pass
        mt.end()


copyParentDirs(H)
