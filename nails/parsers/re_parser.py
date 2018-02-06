# coding=utf-8


def parse_by_regex_with_span(regex, text):
    return [(m.group(0), (m.span())) for m in regex.finditer(text)]
