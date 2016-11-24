# coding=utf-8
from __future__ import unicode_literals

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


def list_files(directory, pattern=None):
    wd = os.path.realpath(directory)
    return glob.glob(os.path.join(wd, pattern))
