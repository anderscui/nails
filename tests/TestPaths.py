# coding=utf-8
from nails.paths import list_files, list_files_rec
from tests.BaseTestCase import BaseTestCase


class TestPaths(BaseTestCase):

    def test_list_files(self):
        for f in list_files('.', '*.py'):
            print(f)

    def test_list_files_rec(self):
        for f in list_files_rec('.', '*.py'):
            print(f)
