#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

from reconfigure import __version__

setup(
    name='reconfigure',
    version=__version__,
    install_requires=[
        'chardet',
    ],
    description='An ORM for config files',
    author='Eugeny Pankov',
    author_email='e@ajenti.org',
    url='http://ajenti.org/',
    packages=find_packages(exclude=['*test*']),
)
