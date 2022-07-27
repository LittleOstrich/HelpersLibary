import os
import shutil

from pathlib import Path


def dirsExist(args):
    for arg in args:
        srcDirExists = os.path.isdir(arg)
        if not srcDirExists:
            print("SrcDir does not exists: ", arg)
            assert False


def removeDir(src):
    try:
        shutil.rmtree(src)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (src, e))
        raise e


def cleanUpFolders(folders):
    for folder in folders:
        assert ("tools" not in folder)
        assert ("helpers" not in folder)
        if not os.path.isdir(folder):
            continue
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))


def prepFolderReport(src):
    ds, _ = recursiveWalk(src)
    N = len(ds)
    for i in range(N):
        pass


def recursiveWalk(sD=".", fileFilter=None, debug=False):
    fs = set()
    ds = set()
    for root, dirs, files in os.walk(sD):
        for name in files:
            fp = os.path.join(root, name)
            fs.add(fp)
        for dir in dirs:
            dp = os.path.join(root, dir)
            ds.add(dp)
    ds = list(ds)
    fs = list(fs)

    dsTmp = list()
    fsTmp = list()
    if fileFilter is not None:
        for f in fs:
            if fileFilter(f):
                fsTmp.append(f)
        fs = fsTmp
        ds = dsTmp

    if debug:
        for d in ds:
            print(d)
        for f in fs:
            print(f)

    return ds, fs


def recursiveWalk2(sD=".", fileFilter=None, debug=False):
    fs = set()
    ds = set()
    for root, dirs, files in os.walk(sD):
        for name in files:
            fp = os.path.join(root, name)
            if fileFilter is None:
                fs.add(fp)
            else:
                if fileFilter(fp):
                    fs.add(fp)
        for dir in dirs:
            dp = os.path.join(root, dir)
            if fileFilter is None:
                ds.add(dp)
            else:
                if fileFilter(dp):
                    ds.add(dp)
    ds = list(ds)
    fs = list(fs)
    if debug:
        for d in ds:
            print(d)
        for f in fs:
            print(f)
    return ds, fs


class DisplayablePath(object):
    display_filename_prefix_middle = '├──'
    display_filename_prefix_last = '└──'
    display_parent_prefix_middle = '    '
    display_parent_prefix_last = '│   '

    def __init__(self, path, parent_path, is_last):
        self.path = Path(str(path))
        self.parent = parent_path
        self.is_last = is_last
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    @classmethod
    def make_tree(cls, root, parent=None, is_last=False, criteria=None):
        root = Path(str(root))
        criteria = criteria or cls._default_criteria

        displayable_root = cls(root, parent, is_last)
        yield displayable_root

        children = sorted(list(path
                               for path in root.iterdir()
                               if criteria(path)),
                          key=lambda s: str(s).lower())
        count = 1
        for path in children:
            is_last = count == len(children)
            if path.is_dir():
                yield from cls.make_tree(path,
                                         parent=displayable_root,
                                         is_last=is_last,
                                         criteria=criteria)
            else:
                yield cls(path, displayable_root, is_last)
            count += 1

    @classmethod
    def _default_criteria(cls, path):
        return True

    def displayable(self):
        if self.parent is None:
            return self.displayname

        _filename_prefix = (self.display_filename_prefix_last
                            if self.is_last
                            else self.display_filename_prefix_middle)

        parts = ['{!s} {!s}'.format(_filename_prefix,
                                    self.displayname)]

        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(self.display_parent_prefix_middle
                         if parent.is_last
                         else self.display_parent_prefix_last)
            parent = parent.parent

        return ''.join(reversed(parts))


def foldersExsists(dirs):
    N = len(dirs)
    isOk = True
    for i in range(N):
        s = dirs[i]
        try:
            assert os.path.isdir(s)
        except Exception as e:
            print("Creating the following folder: ", s)
            os.makedirs(s, exist_ok=True)

    return isOk


def copyFolderStructure(src, dst):
    dirs, _ = recursiveWalk(src)
    N = len(dirs)
    srcDir = src.split(os.sep)[-1]
    for i in range(N):
        d = dirs[i]
        d = d.replace(src, dst + os.sep + srcDir)
        dirs[i] = d
        print("Creating directory: ", d)
        os.makedirs(d, exist_ok=True)
