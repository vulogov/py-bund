import os
from setuptools import setup, find_packages

name="bund"
version="0.0"
release="0.0.1"


setup(name=name,
    setup_requires=['pytest-runner'],
    test_require=['pytest'],
    version=release,
    description='BUND language interpreter library',
    url='https://github.com/vulogov/py-bund',
    author='Vladimir Ulogov',
    author_email='vulogov@linkedin.com',
    license='GPL3',
    packages=find_packages())
