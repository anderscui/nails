# coding=utf-8
from nails.texts import remove_prefix, remove_postfix
from tests.BaseTestCase import BaseTestCase


class TestTexts(BaseTestCase):

    def test_remove_prefix(self):
        s = 'helloworld'
        self.assertEqual(remove_prefix(s, 'hello'), 'world')

    def test_remove_postfix(self):
        s = 'helloworld'
        self.assertEqual(remove_postfix(s, 'world'), 'hello')
