# coding=utf-8
import glob
import os


class File(object):
    def __init__(self, path):
        self.original = path
        self.abspath = os.path.abspath(path)

    def __str__(self):
        prefix = ''
        if self.isfile:
            prefix = 'file: '
        elif self.isdir:
            prefix = 'dir: '
        return prefix + self.original

    def dir_required(self):
        if not self.isdir:
            raise ValueError('Only dir is supported for this operation.')

    def file_required(self):
        if not self.isfile:
            raise ValueError('Only file is supported for this operation.')

    @staticmethod
    def join(path, *paths):
        return os.path.join(path, *paths)

    @property
    def name(self, without_ext=False):
        return os.path.basename(self.abspath)

    @property
    def name_without_ext(self):
        basename = os.path.basename(self.abspath)
        return os.path.splitext(basename)[0]

    @property
    def ext(self):
        return os.path.splitext(self.abspath)[1]

    @property
    def isfile(self):
        return os.path.isfile(self.abspath)

    @property
    def isdir(self):
        return os.path.isdir(self.abspath)

    @property
    def exists(self):
        return os.path.exists(self.abspath)

    def find(self, pattern='*'):
        self.dir_required()
        wd = os.path.realpath(self.abspath)
        return [File(f) for f in glob.glob(os.path.join(wd, pattern))]

    def subdirs(self):
        self.dir_required()
        return [f for f in self.find() if f.isdir]

    def files(self, pattern='*'):
        self.dir_required()
        return [f for f in self.find(pattern) if f.isfile]

    def create_if_not_exists(self):
        if not self.exists:
            os.makedirs(self.abspath)

    def remove(self):
        if self.isdir:
            os.removedirs(self.abspath)
        else:
            os.remove(self.abspath)

    def write(self, s, mode='w', encoding='utf-8'):
        with open(self.abspath, mode=mode, encoding=encoding) as f:
            f.write(s)

    def writelines(self, lines, mode='w', encoding='utf-8'):
        with open(self.abspath, mode=mode, encoding=encoding) as f:
            f.writelines(lines)

    def append(self, s):
        self.write(s, 'a')

    def appendlines(self, lines):
        self.writelines(lines, 'a')

    def readlines(self, mode='r', encoding='utf-8'):
        with open(self.abspath, mode, encoding=encoding) as f:
            for line in f:
                yield line

    # read json
    # write json
    # pickle?
    # create tmp

    # move to
    # iterable
