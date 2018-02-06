# coding=utf-8
from __future__ import unicode_literals

from operator import itemgetter


class ElementNotFound(ValueError):

    def __init__(self, msg):
        self.strerror = msg
        # self.args = {msg}


class DuplicateError(ValueError):
    """Raised when duplicate value is added to a distinctdict"""


class distinctdict(dict):
    """Dictionry that does not accept duplicate values."""
    def __setitem__(self, key, value):
        if value in self.values():
            if (key in self and self[key] != value) or key not in self:
                raise DuplicateError('This value already exists for diff key')

        super().__setitem__(key, value)


def index_of(iterator, pred):
    for i, elem in enumerate(iterator):
        if pred(elem):
            return i
    return -1


def find_next(iterator, pred, default=None):
    for i, elem in enumerate(iterator):
        if pred(elem):
            return elem
    return default


def all(iterable, pred):
    return all(pred(item) for item in iterable)


def any(iterable, pred):
    return any(pred(item) for item in iterable)


def next(iterable, pred, default=None):
    for item in iterable:
        if pred(item):
            return item
    return default


def count(iterable, pred):
    return sum([1 if pred(item) else 0 for item in iterable])


fst = itemgetter(0)
snd = itemgetter(1)


def nth(n):
    return itemgetter(n-1)
