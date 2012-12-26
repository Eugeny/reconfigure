#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(
    name='reconfigure',
    version='1.0',
    install_requires=[
        'iniparse',
    ],
    description='An ORM for config files',
    author='Eugeny Pankov',
    author_email='e@ajenti.org',
    url='http://ajenti.org/',
    packages=find_packages(exclude=['*test*']),
)
