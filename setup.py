import os
from setuptools import setup, find_packages


setup(name='bund',
    setup_requires=['pytest-runner'],
    test_require=['pytest'],
    version='0.1',
    description='BUND language interpreter library',
    url='https://github.com/vulogov/py-bund',
    author='Vladimir Ulogov',
    author_email='vulogov@linkedin.com',
    license='GPL3',
    packages=find_packages())
