import sys
import os
import platform
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from bund.library.ns import *
from bund.library.data import *
from bund.language import bundInit, bundParse
from bund.vm.scripts import *
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

def test_vm_ha3():
    namespace = bundInit()
    namespace = bundParse(namespace, """[/HELLO> ;;""")
    assert isinstance(namespace["HELLO"], dict)

def test_vm_ha4():
    namespace = bundInit()
    namespace = vmScript(namespace, 'main', """[/HELLO> ;;""")
    namespace = bundParse(namespace, 'main', script=True)
    assert isNamespace(namespace, "/HELLO") == True

def test_vm_ha5():
    namespace = bundInit()
    namespace = vmScript(namespace, 'Main', """[/HELLO> ;;""")
    namespace = bundParse(namespace)
    assert isNamespace(namespace, "/HELLO") == True

def test_vm_ha6():
    namespace = bundInit()
    namespace = vmScript(namespace, 'bootstrap', """[/HELLO> ;;""")
    namespace = bundParse(namespace)
    assert isNamespace(namespace, "/HELLO") == True

def test_vm_ha7():
    namespace = bundInit()
    namespace = bundParse(namespace, """2 2""")
    assert len(nsScript(namespace)) == 5

def test_vm_ha8():
    namespace = bundInit()
    namespace = bundParse(namespace, """2 2""")
    assert len(nsScript(namespace)["script"]) == 2
