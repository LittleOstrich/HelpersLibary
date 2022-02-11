import os

from helpers.folderTools import copyFolderStructure

base = "C:\\Users\\geiss\\OneDrive\\Desktop"
src = base + os.sep + "AramisData"
dst = base + os.sep + "AramisDataTmp"

copyFolderStructure(src, dst)
