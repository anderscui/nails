# coding=utf-8

from setuptools import setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))


def get_version(version_tuple):
    if not isinstance(version_tuple[-1], int):
        return '.'.join(map(str, version_tuple[:-1])) + version_tuple[-1]

    return '.'.join(map(str, version_tuple))


init = os.path.join(here, 'nails', '__init__.py')
version_line = list(filter(lambda l: l.startswith('VERSION'), open(init)))[0]
VERSION = get_version(eval(version_line.split('=')[-1]))

# Get the long description from the README file
with codecs.open(os.path.join(here, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nails',
    version='0.0.1',
    description='common tools in Python',
    long_description=long_description,

    packages=['nails'],

    author='Anders Cui',
    author_email='anderscui@gmail.com',

    url='https://github.com/anderscui/nails',

    keywords='common tools',

    license='MIT License',

    setup_requires=[
    ],
    install_requires=[
    ],
    package_dir={'nails': 'nails'},
    package_data={'nails': ['*.*']}
)

# build: python setup.py bdist_wheel --universal
# install: pip install --upgrade --no-deps --force-reinstall ...
