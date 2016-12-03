import unittest


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # print('setup class...')
        pass

    def setUp(self):
        # print('setup case...')
        pass
