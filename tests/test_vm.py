import sys
import os
import platform
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from bund.ast.parser import parser
from bund.vm.vm import *
from bund.library.ns import *
from bund.library.log import *

def test_vm_1():
    namespace = parser("""[/HELLO> ;;""")
    namespace = vmNew(namespace)
    assert platform.system() == nsGet(namespace, "/sys/vm.os.system")

def test_vm_2():
    namespace = nsCreate()
    namespace = logInit(namespace, 'DEBUG')
    namespace = vmNew(namespace)
    namespace = parser("""[/HELLO> ;;""", namespace)
    assert True == nsGet(namespace, "/sys/bund/is.ready")

def test_vm_log_1():
    namespace = nsCreate()
    namespace = logInit(namespace, 'DEBUG')
    namespace = vmNew(namespace)
    namespace = parser("""[/HELLO> ;;""", namespace)
    assert True == nsGet(namespace, "/sys/log/ready")
