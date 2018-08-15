# coding=utf-8
import os
import re

from nails.filestore import read_lines
from nails.paths import list_files

RE_IDENTIFIER = re.compile(r'^[^\d\W]\w*\Z', re.U)
RE_IMPORT = re.compile(r'import\s+(?P<from>[^\d\W]\w*(\.([^\d\W]\w*))*)', re.U)
RE_FROM_IMPORT = re.compile(r'from\s+(?P<from>[^\d\W]\w*(\.([^\d\W]\w*))*)\s+import\s+(?P<import>.+)', re.U)


def show_counter(counter, ordered_by_key=True):
    if ordered_by_key:
        keys = sorted(counter.keys())
        for k in keys:
            print('{0}: {1}'.format(k, counter[k]))
    else:
        for k in counter.most_common():
            print('{0}: {1}'.format(k[0], k[1]))
    print('')


def counter_less(counter, less_than):
    for k, c in counter.most_common():
        if c < less_than:
            yield k, c


def counter_range(counter, start, end=None):
    for i, p in enumerate(counter.most_common()):
        if i >= start:
            yield p


def show_dict(d, ordered_by_key=True):
    keys = sorted(d.keys()) if ordered_by_key else d.keys()
    for k in keys:
        print('{}: {}'.format(k, d[k]))


def show_imports(p):
    if p.endswith('.py'):
        paths = [os.path.realpath(p)]
    else:
        paths = list_files(p, '*.py')

    result = []
    for file_path in paths:
        for line in read_lines(file_path):
            line = line.strip()
            if not line.startswith('#') and 'import ' in line:
                result.append(line)
    return sorted(set(result))


def is_identifier(s):
    return bool(RE_IDENTIFIER.search(s))


def extract_import(s):
    s = s.strip() if s else ''
    if not s or s.startswith('#') or 'import ' not in s:
        return None

    m = None
    if s.startswith('import '):
        m = RE_IMPORT.search(s)
    elif s.startswith('from '):
        m = RE_FROM_IMPORT.search(s)

    return m.group('from') if m else None


if __name__ == '__main__':
    for imp in show_imports('/Users/andersc/github/cvparse'):
        print(imp)
        ei = extract_import(imp)
        if ei:
            print(ei)
        print()
    # show_imports('__init__.py')
    # print(is_identifier('a1'))
    # print(is_identifier('_a1'))
    # print(is_identifier('var _a1'))
    # print(is_identifier('var 1_a1'))

    # print(is_import('import os').group(1))
    # print(is_import('import pandas').group(1))
    # print(is_import('import jieba.posseg as pseg').group(1))
