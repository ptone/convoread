#!/usr/bin/env python

import os
from setuptools import setup
import convoread

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'convoread',
    description = 'Simple console reader for Convore',
    long_description = read('README.rst'),
    license = 'MIT',
    version = convoread.__version__,
    author = 'foobarbuzz group',
    author_email = 'foobarbuzz@googlegroups.com',

    url = 'https://github.com/foobarbuzz/convoread',

    classifiers = [
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Communications :: Chat',
        ],
    platforms='any',

    packages = ['convoread'],
    entry_points = {'console_scripts': ['convoread = convoread:main']},
    )
