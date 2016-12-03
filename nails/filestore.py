# coding=utf-8
from __future__ import unicode_literals

import json
import pickle


def json_dump(obj, path, mode='w', encoding='utf-8', ensure_ascii=False):
    json.dump(obj, open(path, mode=mode, encoding=encoding), ensure_ascii=ensure_ascii)


def json_dumps(obj, ensure_ascii=False):
    return json.dumps(obj, ensure_ascii=ensure_ascii)


def json_load(path, mode='r', encoding='utf-8'):
    return json.load(open(path, mode=mode, encoding=encoding))


def json_loads(s, encoding='utf-8'):
    return json.loads(s, encoding=encoding)


# TODO: pickle
