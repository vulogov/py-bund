import sys
import os
import platform
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from bund.language import bundInit
from bund.vm.config import *

def test_vm_ha1():
    namespace = bundInit()
    data = vmConfigGet(namespace, "builtinmodules.path")
    assert data == sys.path

def test_vm_ha2():
    namespace = bundInit()
    vmConfigAppend(namespace, "builtinmodules.path", ".")
    data = vmConfigGet(namespace, "builtinmodules.path")
    assert data[-1] == "."
