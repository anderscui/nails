# coding=utf-8
import fnmatch
import hashlib
import os
import glob


def file_ext(filename):
    """
    Gets extension from path, with the '.'
    :param filename:
    :return:
    """
    return os.path.splitext(filename)[1]


def file_name(filename):
    """
    Gets file name without extension.
    :param filename:
    :return: file name.
    """
    return os.path.splitext(filename)[0]


def path_leaf(path):
    parts = os.path.split(path)
    if parts:
        return parts[-1]
    else:
        return os.path.basename(path)


def list_files(directory, pattern="*.*"):
    wd = os.path.realpath(directory)
    return glob.glob(os.path.join(wd, pattern))


def list_files_rec(directory, pattern='*.*'):
    abs_dir = os.path.abspath(directory)
    for root, subdirs, files in os.walk(abs_dir):
        for f in fnmatch.filter(files, pattern):
            yield os.path.join(root, f)


def file_hash(path, algorithm='sha256'):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()
