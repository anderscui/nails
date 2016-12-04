# coding=utf-8
from __future__ import unicode_literals


def show_counter(counter, ordered_by_key=True):
    if ordered_by_key:
        keys = sorted(counter.keys())
        for k in keys:
            print('{0}: {1}'.format(k, counter[k]))
    else:
        for k in counter.most_common():
            print('{0}: {1}'.format(k[0], k[1]))
    print('')


def show_dict(d, ordered_by_key=True):
    keys = sorted(d.keys()) if ordered_by_key else d.keys()
    for k in keys:
        print('{}: {}'.format(k, d[k]))
