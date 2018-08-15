# coding=utf-8
import re

RE_WHITESPACE = re.compile(r"(\s)+", re.UNICODE)


def remove_postfix(s, postfix):
    if s.endswith(postfix):
        return s[:len(s)-len(postfix)]


def remove_prefix(s, prefix):
    if s.startswith(prefix):
        return s[len(prefix):]


def flatten2str(obj):
    if obj is None:
        return ''
    if isinstance(obj, str):
        return obj
    if isinstance(obj, (list, tuple)):
        return ' '.join(obj)
    return str(obj)


def compress_whitespaces(s):
    return RE_WHITESPACE.sub(' ', s)
