import sys
import os
import platform
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from bund.ast.parser import parser
from bund.vm.vm import *
from bund.library.ns import *

def test_vm_1():
    namespace = parser("""[/HELLO> ;;""")
    namespace = vmNew(namespace)
    assert platform.system() == nsGet(namespace, "/sys/vm.os.system")

def test_vm_2():
    namespace = parser("""[/HELLO> ;;""")
    namespace = vmNew(namespace)
    assert True == nsGet(namespace, "/sys/default/is.ready")
