import os

import shutil

from helpers.folderTools import recursiveWalk, dirsExist
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


def copyProject(src, dst, allowedFileEndings=None, ignoreFolder=None, debug=False):
    ds, fs = recursiveWalk(src)

    for d in ds:
        relDir = os.path.relpath(d, src)
        newFp = dst + os.sep + relDir

        br = False
        if ignoreFolder is not None:
            for iF in ignoreFolder:
                if iF in newFp:
                    br = True
                    break
        if br:
            continue

        if debug:
            print("dir")
            print(d)
            print(newFp)
            print("-")
        else:
            os.makedirs(newFp, exist_ok=True)

    for f in fs:
        fe = f.split(".")[-1]
        if fe in allowedFileEndings or allowedFileEndings is None:
            relDir = os.path.relpath(f, src)
            newFp = dst + os.sep + relDir
            br = False
            if ignoreFolder is not None:
                for iF in ignoreFolder:
                    if iF in newFp:
                        br = True
                        break
            if br:
                continue

            if debug:
                print("file")
                print(f)
                print(newFp)
                print("-")
            else:
                copyFile(f, newFp)


def remove_files(files):
    for file in files:
        if os.path.isfile(file):
            os.remove(file)


def isCsv(s: str):
    ret = s.endswith(".csv")
    return ret


def copyFile(src, dst):
    shutil.copyfile(src, dst)


def copyFiles(src, dst, filter=lambda x: True, debug=False):
    mt = myTimer("copyFiles")
    mt.start()
    dirsExist([src, dst])

    _, fs = recursiveWalk(src, fileFilter=filter)
    N = len(fs)
    cfc = 0  # copiedFilesCount
    ncfc = 0  # notCopiedFilesCount
    okFiles = 0
    notOkFiles = 0
    for i in range(N):
        f = fs[i]
        isOk = filter(f)

        if isOk:
            okFiles = okFiles + 1
            tail = f.replace(src, "")
            newDst = dst + tail
            if os.path.isfile(newDst):
                ncfc = ncfc + 1
                continue
            else:
                shutil.copy(f, newDst)
                cfc = cfc + 1
            if debug:
                print("src: ", src)
                print("dst: ", newDst)
        else:
            notOkFiles = notOkFiles + 1

    print("Total number of files found: ", N)
    print("Files copied: ", cfc)
    print("Files not copied: ", ncfc)
    print("Files ok to copy: ", okFiles)
    print("Files not ok to copy: ", notOkFiles)
    print("-------------")
    # lists = mt.end()
    # listsToCsv(lists, dstDir="tmp", name="runTimeReport", withDate=True)
