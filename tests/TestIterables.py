# coding=utf-8
from collections import defaultdict

from tests.BaseTestCase import BaseTestCase
from nails.iterables import find_next, index_of, fst, snd, nth


class TestIterables(BaseTestCase):
    def test_first_elem(self):
        pairs = [('person_name', '王小波'), ('company_name', '露一'), ('job_title', '数据分析师'),
                 ('org_name', '同济大学'), ('person_name', '催眠'), ('time', '2013年')]

        self.assertEqual(next(p for p in pairs if p[0] == 'person_name')[1], '王小波')
        self.assertIsNone(next((p for p in pairs if p[0] == 'person_namef'), None))

    def test_set(self):
        s = set()
        s.add(1)
        s.add(2)
        print(s)

        s.add(3)
        print(s)

    def test_defaultdict(self):
        d = defaultdict(defaultdict)
        print(d)

    def test_all(self):
        l1 = [1, 2, 3]
        self.assertTrue(all(i < 5 for i in l1))

    def test_any(self):

        l1 = [1, 2, 3]
        self.assertTrue(any(i > 2 for i in l1))

    def test_max(self):
        sl = ['apple', 'banana', 'pear']
        max_len = max(sl, key=lambda s: len(s))
        self.assertEqual(max_len, 'banana')

    def test_min(self):
        tl = [(3, 'apple'), (5, 'banana'), (6, 'pear')]
        min_elem = min(tl, key=lambda t: len(t[1]))
        self.assertEqual(min_elem, (6, 'pear'))

    def test_find_next(self):
        strs = ['one', 'two', 'three']
        elem = find_next(strs, lambda s: s.startswith('t'))
        self.assertEqual(elem, 'two')

        elem = find_next(strs, lambda s: s.startswith('w'))
        self.assertIsNone(elem)

    def test_index_of(self):
        strs = ['one', 'two', 'three']
        i = index_of(strs, lambda s: s.startswith('t'))
        self.assertEqual(i, 1)

        i = index_of(strs, lambda s: s.startswith('w'))
        self.assertEqual(i, -1)

    def test_nth(self):
        nums = range(1, 10)
        self.assertEqual(fst(nums), 1)
        self.assertEqual(snd(nums), 2)
        self.assertEqual(nth(5)(nums), 5)
