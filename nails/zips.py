# coding=utf-8
from zipfile import ZipFile

with open('/Users/andersc/Downloads/movie/more_movies2.zip', 'rb') as f:
    z = ZipFile(f)
    for name in z.namelist():
        print(name)
        # z.extract(name, './')
