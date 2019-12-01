import sys
import os
import platform
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from bund.language import bundInit, bundParse
from bund.vm.vm import *
from bund.vm.builtins import *
from bund.library.data import *
from bund.ast.parser import *
from bund.library.data import *
from bund.vm.eval import vmEval

def test_stack_1():
    namespace = bundInit()
    namespace = bundParse(namespace, """2 3 ==?""")
    namespace = vmEval(namespace, "__script__")
    size = vmPull(namespace)
    assert dataValue(size) == 2

def test_stack_2():
    namespace = bundInit()
    namespace = bundParse(namespace, """2 3 % 1 ==?""")
    namespace = vmEval(namespace, "__script__")
    size = vmPull(namespace)
    assert dataValue(size) == 1

def test_stack_3():
    namespace = bundInit()
    namespace = bundParse(namespace, """2 3 % ==> 1  ==?""")
    namespace = vmEval(namespace, "__script__")
    size = vmPull(namespace)
    assert dataValue(size) == 3
