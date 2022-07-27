import os

from helpers.fileTools import copyProject
from helpers.folderTools import copyFolderStructure


def run1():
    base = "C:\\Users\\geiss\\OneDrive\\Desktop"
    src = base + os.sep + "AramisData"
    dst = base + os.sep + "AramisDataTmp"

    copyFolderStructure(src, dst)


def run2():
    src = r'C:\Users\geiss\Desktop\LainProject\Python\HelpersLibary'
    dst = r'C:\Users\geiss\Desktop\LainProject\Python\HelpersLibary\snippets\tmp\HelpersLibrary'
    allowedFileEndings = ["py", "csv"]
    ignoreFolder = [".git", "__pycache__", ".idea"]
    debug = False
    copyProject(src=src,
                dst=dst,
                allowedFileEndings=allowedFileEndings,
                ignoreFolder=ignoreFolder,
                debug=debug)


run2()
