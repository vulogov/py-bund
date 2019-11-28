import sys
import os
import platform
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from bund.language import bundInit
from bund.vm.vm import *
from bund.vm.builtins import *
from bund.library.data import *

def test_b_1():
    namespace = bundInit()
    namespace = vmBuiltinModule(namespace, "Time")

def test_b_2():
    namespace = bundInit()
    namespace = vmBuiltinModule(namespace, "Time")
    mod = vmBuiltinGet(namespace, "Time")
    assert dataIsType(mod, builtin_module) == True

def test_b_3():
    namespace = bundInit()
    namespace = vmBuiltinModule(namespace, "Time")
    fun = vmBuiltinGet(namespace, "Time.Now")
    assert dataIsType(fun, builtin_function) == True

def test_b_4():
    namespace = bundInit()
    namespace = vmBuiltinModule(namespace, "Time")
    fun = dataValue(vmBuiltinGet(namespace, "Time.Now"))
    fun(namespace)
    data = vmPull(namespace)
    assert dataIsType(data, float) == True

def test_b_5():
    namespace = bundInit()
    namespace = vmBuiltinModule(namespace, "Time")
    fun = dataValue(vmBuiltinGet(namespace, "/Time/Now"))
    fun(namespace)
    data = vmPull(namespace)
    assert dataIsType(data, float) == True

def test_b_6():
    namespace = bundInit()
    assert len(vmBuiltinList(namespace)) > 0
