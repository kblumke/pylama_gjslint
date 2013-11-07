#!/usr/bin/env python

""" Support gjslint code checker.

pylama_gjslint
-------------

pylama_gjslint -- gjslint integration to pylama library.

"""

from os import path as op

from setuptools import setup, find_packages
from pylama_gjslint import __version__, __project__, __author__, __license__


def read(fname):
    try:
        return open(op.join(op.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name=__project__,
    version=__version__,
    license=__license__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    platforms=('Any'),
    author='trojkat',
    author_email='tomasz@karbownicki.com',
    url='http://github.com/trojkat/pylama_gjslint',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    entry_points={
        'pylama.linter': [
            'gjslint = pylama_gjslint.main:Linter',
        ],
    },
    packages=find_packages(),
    install_requires = [
        l for l in read('requirements.txt').split('\n')
        if l and not l.startswith('#')],
)

# lint_ignore=F0401
