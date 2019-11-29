import sys
import os
import platform
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from bund.library.data import *
from bund.language import bundInit
from bund.vm.python import *
from bund.vm.vm import *

def test_py_1():
    namespace = bundInit()
    fun = pyImportFun(namespace, 'bund.vm.bund.stdlib.Time', 'Now')
    assert isinstance(fun, dict) == True

def test_py_2():
    namespace = bundInit()
    fun = pyImportFun(namespace, 'bund.vm.lang.bund.stdlib.Time', 'Now')
    have_fun = "Now" in fun
    assert  have_fun == True

def test_py_3():
    namespace = bundInit()
    fun = pyImportFun(namespace, 'bund.vm.lang.bund.stdlib.Time', 'Now')
    assert  dataIsType(fun["Now"], python_function) == True

def test_py_4():
    namespace = bundInit()
    fun = pyImportFun(namespace, 'bund.vm.lang.bund.stdlib.Time', 'Now')
    dataValue(fun["Now"])(namespace)
    data = vmPull(namespace)
    assert dataIsType(data, float) == True
