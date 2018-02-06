# coding=utf-8
from nails.parsers.nums import *
from tests.BaseTestCase import BaseTestCase


class TestTexts(BaseTestCase):

    def test_parse_nums(self):
        s = '2010年世界杯的32支球队'
        self.assertEqual(len(parse_ints(s)), 2)

    def test_parse_decimals(self):
        s = '.11 < 1.11 3点1'
        self.assertEqual(len(parse_decimals(s)), 2)

    def test_ages(self):
        s = '这棵树已有120岁了'
        print(parse_ages(s))

    def test_parse_cellphones(self):
        s = '号码13212344321拍'
        print(parse_cellphones(s))
