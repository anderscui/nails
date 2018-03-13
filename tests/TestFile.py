# coding=utf-8
import os
import unittest

from tests.BaseTestCase import BaseTestCase
from nails.filesystem import File


class TestFile(BaseTestCase):

    def getcwd(self):
        fname = __file__
        return os.path.split(fname)[0]

    def test_file(self):
        fname = __file__
        name = os.path.basename(fname)
        fd = os.path.split(fname)[0]

        f = File(fname)
        self.assertEqual(f.original, fname)
        self.assertEqual(f.abspath, fname)
        self.assertEqual(f.name, name)
        self.assertEqual(f.name_without_ext, 'TestFile')

        self.assertEqual(f.ext, '.py')

        self.assertTrue(f.exists)
        self.assertTrue(f.isfile)
        self.assertFalse(f.isdir)

    def test_dir(self):
        fname = __file__
        fd = os.path.split(fname)[0]

        d = File(fd)
        items = d.find('*')
        self.assertIn(fname, [item.abspath for item in items])
        self.assertIn(File.join(fd, 'data'), [item.abspath for item in items])

        subdirs = d.subdirs()
        self.assertIn(File.join(fd, 'data'), [item.abspath for item in subdirs])

        pyfiles = d.files('*.py')
        self.assertTrue(len(pyfiles) > 0)
        self.assertTrue(all(f.ext == '.py' for f in pyfiles))

    def test_create_if_not_exists(self):
        fname = __file__
        fd = os.path.split(fname)[0]
        tempdir = File(File.join(fd, 'tempdir'))
        self.assertFalse(tempdir.exists)
        tempdir.create_if_not_exists()
        self.assertTrue(tempdir.exists)
        tempdir.remove()
        self.assertFalse(tempdir.exists)

    def test_remove_file(self):
        fname = __file__
        f = File(os.path.join(os.path.split(fname)[0], 'test.txt'))
        if f.exists:
            f.remove()
            self.assertFalse(f.exists)

    def test_write(self):
        fname = __file__
        f = File(os.path.join(os.path.split(fname)[0], 'data/test.txt'))
        f.write('行line')

    def test_append(self):
        fname = __file__
        f = File(os.path.join(os.path.split(fname)[0], 'data/test.txt'))
        f.append('一行line1\n')
        f.append('line2\n')

    def test_writelines(self):
        fname = __file__
        f = File(os.path.join(os.path.split(fname)[0], 'data/test.txt'))
        f.writelines(['一行line\n' for i in range(5)])

    def test_appendlines(self):
        fname = __file__
        f = File(os.path.join(os.path.split(fname)[0], 'data/test.txt'))
        f.appendlines(['新行line\n' for i in range(5)])

    def test_readlines(self):
        f = File(File.join(self.getcwd(), 'data/test.txt'))
        for l in f.readlines():
            print(l.strip())

if __name__ == '__main__':
    unittest.main()
