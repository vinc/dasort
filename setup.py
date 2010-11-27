#!/usr/bin/env python

from distutils.core import setup

setup(name='DaSort',
    version='0.0.1',
    description='A CLI tool for sorting and grouping picture by date',
    author='Vincent Ollivier',
    author_email='contact@vincentollivier.com',
    url='https://github.com/vinc/dasort',
    packages=['dasort'],
    scripts=['scripts/dasort']
)
