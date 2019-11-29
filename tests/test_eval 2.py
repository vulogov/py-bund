import sys
import os
import platform
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from bund.language import bundInit, bundParse
from bund.vm.eval import vmEval
from bund.vm.vm import vmStack, vmArguments
from bund.library.data import *

def test_eval_1():
    namespace = bundInit()
    namespace = bundParse(namespace, """2 2""")
    namespace = vmEval(namespace, "__script__")
    namespace = vmStack(namespace)
    assert len(vmArguments(namespace)) == 2

def test_eval_2():
    namespace = bundInit()
    namespace = bundParse(namespace, """41 1 % 1 2 3""")
    namespace = vmEval(namespace, "__script__")
    namespace = vmStack(namespace)
    assert len(vmArguments(namespace)) == 3

def test_eval_3():
    namespace = bundInit()
    namespace = bundParse(namespace, """
    "Hello"
    "World"
    """)
    namespace = vmEval(namespace, "__script__")
    namespace = vmStack(namespace)
    assert len(vmArguments(namespace)) == 2

def test_eval_4():
    namespace = bundInit()
    namespace = bundParse(namespace, "/Time/Now")
    namespace = vmEval(namespace, "__script__")
    namespace = vmStack(namespace)
    assert dataType(vmArguments(namespace)[0]) == 'float'
