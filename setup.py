# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from distutils.core import Command
from unittest import TextTestRunner, TestLoader
from os import path

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()


class TestCommand(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        loader = TestLoader()
        suite = loader.discover('pynes/tests', pattern='*_test.py')
        TextTestRunner(verbosity=4).run(suite)


setup(
    name='pyNES',
    version='0.0.2',
    description='Python Programming for Nintendo 8bits',
    long_description=long_description,
    author="Gustavo Maia Neto (Guto Maia)",
    author_email="guto@guto.net",
    license="GPL3",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "examples"]),
    scripts=['bin/pynes'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Programming Language :: Assembly',
        'Topic :: Games/Entertainment',
        'Topic :: Software Development :: Assemblers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Embedded Systems',
    ],
    url='http://github.com/gutomaia/pyNES/',
    cmdclass={'test': TestCommand},
    test_suite="pynes.tests",
)
