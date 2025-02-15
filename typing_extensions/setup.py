#!/usr/bin/env python
# coding: utf-8

import sys
from setuptools import setup

if sys.version_info < (3, 6, 0):
    sys.stderr.write('ERROR: You need Python 3.6+ '
                     'to install typing_extensions.\n')
    exit(1)

version = '3.10.0.2'
description = 'Backported and Experimental Type Hints for Python 3.6+'
long_description = '''\
Typing Extensions -- Backported and Experimental Type Hints for Python

The ``typing`` module was added to the standard library in Python 3.5, but
many new features have been added to the module since then.
This means users of older Python versions who are unable to upgrade will not be
able to take advantage of new types added to the ``typing`` module, such as
``typing.Protocol`` or ``typing.TypedDict``.

The ``typing_extensions`` module contains backports of these changes.
Experimental types that will eventually be added to the ``typing``
module are also included in ``typing_extensions``.
'''

classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Python Software Foundation License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Software Development',
]

setup(name='typing_extensions',
      version=version,
      description=description,
      long_description=long_description,
      author='Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee',
      author_email='levkivskyi@gmail.com',
      url='https://github.com/python/typing/blob/master/typing_extensions/README.rst',
      license='PSF',
      keywords='typing function annotations type hints hinting checking '
               'checker typehints typehinting typechecking backport',
      package_dir={'': 'src_py3'},
      py_modules=['typing_extensions'],
      classifiers=classifiers,
      )
