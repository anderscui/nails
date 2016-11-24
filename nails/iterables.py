# coding=utf-8
from __future__ import unicode_literals


def index_of(iterator, pred):
    for i, elem in enumerate(iterator):
        if pred(elem):
            return i
    return -1


def show_counter(counter, ordered_by_key=True):
    if ordered_by_key:
        keys = sorted(counter.keys())
        for k in keys:
            print('{0}: {1}'.format(k, counter[k]))
    else:
        for k in counter.most_common():
            print('{0}: {1}'.format(k[0], k[1]))
    print('')


def remove_empty_keys(counter):
    empty_keys = [k for k in counter if not k or not k.strip()]
    for ek in empty_keys:
        del counter[ek]
