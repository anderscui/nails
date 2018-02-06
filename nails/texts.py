# coding=utf-8
from __future__ import absolute_import, unicode_literals, division


def remove_postfix(s, postfix):
    if s.endswith(postfix):
        return s[:len(s)-len(postfix)]


def remove_prefix(s, prefix):
    if s.startswith(prefix):
        return s[len(prefix):]
