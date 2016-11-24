# coding=utf-8
from __future__ import unicode_literals

import sys

PY2 = sys.version_info[0] == 2

if PY2:
    string_types = (str, unicode)

    iterkeys = lambda d: d.iterkeys()
    itervalues = lambda d: d.itervalues()
    iteritems = lambda d: d.iteritems()

else:
    unicode = str
    string_types = (str,)

    unichr = chr
    xrange = range

    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    iteritems = lambda d: iter(d.items())


if PY2:
    def strdecode(s):
        if not isinstance(s, unicode):
            try:
                s = s.decode('utf-8')
            except UnicodeDecodeError:
                s = s.decode('gbk', 'ignore')
        return s
else:
    strdecode = lambda s: s
