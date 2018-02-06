# coding=utf-8
import re

from nails.parsers.re_parser import parse_by_regex_with_span

RE_PURE_DIGITS = re.compile(r'\d+', re.U)
RE_INT = re.compile(r'(?<!\d)(?P<num>[1-9]\d*)(?!\d)', re.U)
RE_DECIMAL = re.compile(r'(?P<num>([1-9]\d*\.\d+)|(\.\d+))', re.U)

# RE_DECIMAL = re.compile(r'(?P<num>[1-9]\d*)', re.U)
# RE_DECIMAL = re.compile(r'(?P<num>[1-9]\d*)', re.U)
# RE_DECIMAL = re.compile(r'(?P<num>[1-9]\d*)', re.U)


RE_AGE = re.compile(r'(?<!\d)(?P<age>[1-9]\d{1,2})\s*岁', re.U)

RE_CELLPHONE = re.compile(r'(?<!\d)1[34578]\d{9}(?!\d)', re.U)
RE_EMAIL = re.compile(r'[a-z_0-9-][a-z_0-9.-]{0,64}@([a-z0-9-]{1,200}\.){1,5}[a-z]{1,6}', re.U)
RE_IDNO = re.compile(r'((?<!\d)\d{17}([0-9]|X)(?!\d))|((?<!\d)\d{15}(?!\d))', re.U)
RE_URL = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', re.U)
RE_IP = re.compile(r'(?P<num>[1-9]\d*)', re.U)

RE_WORK_YEAR = re.compile(r'(?<!\d)(?P<year>[1-9]{1,2})\s*年', re.U)
RE_GROUP_SIZE = re.compile(r'(\d+\s*-\s*\d+\s*个?人)|(\d+\s*个?人以上)|(\d+\s*个?人左右)', re.U)
RE_SALARY = re.compile(r'((\d+-\d+)元?/月)|((\d+k-\d+k)元?(/月)?)', re.U)

RE_TIME_DELTA = re.compile(r'((\d+-\d+)元?/月)|((\d+k-\d+k)元?(/月)?)', re.U)

UNITS = {'k': 10**3,
         'K': 10**3,
         'w': 10**4,
         'W': 10**4,
         '千': 10**3,
         '万': 10**4,
         '%': 0.01}


def parse_ints(text):
    return parse_by_regex_with_span(RE_INT, text)


def parse_decimals(text):
    return parse_by_regex_with_span(RE_DECIMAL, text)


def parse_ages(text):
    return parse_by_regex_with_span(RE_AGE, text)


def parse_cellphones(text):
    return parse_by_regex_with_span(RE_CELLPHONE, text)
