# coding=utf-8
import os
import re

from nails.filestore import read_lines
from nails.paths import list_files

RE_IDENTIFIER = re.compile(r'^[^\d\W]\w*\Z', re.U)
RE_IMPORT = re.compile(r'import ([^\d\W]\w*(\.([^\d\W]\w*))*)', re.U)


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


def show_imports(p):
    if p.endswith('.py'):
        paths = [os.path.realpath(p)]
    else:
        paths = list_files(p, '*.py')

    result = []
    for file_path in paths:
        for line in read_lines(file_path):
            if 'import ' in line:
                result.append(line.strip())
    return sorted(set(result))


def is_identifier(s):
    return bool(RE_IDENTIFIER.search(s))


def is_import(s):
    return RE_IMPORT.search(s)


if __name__ == '__main__':
    for imp in show_imports('/Users/andersc/github/cvparse'):
        if imp.startswith('#') or not imp.startswith('import'):
            continue

        print(imp)
        print(is_import(imp).group(1))
        print()
    # show_imports('__init__.py')
    # print(is_identifier('a1'))
    # print(is_identifier('_a1'))
    # print(is_identifier('var _a1'))
    # print(is_identifier('var 1_a1'))

    # print(is_import('import os').group(1))
    # print(is_import('import pandas').group(1))
    # print(is_import('import jieba.posseg as pseg').group(1))
