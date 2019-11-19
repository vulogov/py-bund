import sys
import os
import platform
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from bund.ast.parser import parser
from bund.vm.vm import *
from bund.vm.config import *
from bund.vm.localns import *
from bund.vm.template import *
from bund.vm.runtime_vars import vmRtGet, vmRtSet
from bund.library.ns import *
from bund.library.log import *
from bund.library.data import *


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

def test_vm_3():
    namespace = nsCreate()
    namespace = logInit(namespace, 'DEBUG')
    namespace = vmNew(namespace)
    namespace = parser("""[/HELLO> ;;""", namespace)
    vmPush(namespace, 42)
    data = vmPull(namespace)
    assert dataValue(data) == 42
def test_vm_4():
    namespace = nsCreate()
    namespace = logInit(namespace, 'DEBUG')
    namespace = vmNew(namespace)
    namespace = parser("""[/HELLO> ;;""", namespace)
    local = nsGet(namespace, "/HELLO")
    assert lnsIs(local) == True

def test_vm_5():
    namespace = nsCreate()
    namespace = logInit(namespace, 'DEBUG')
    namespace = vmNew(namespace)
    namespace = parser("""[/HELLO> Answer <- 42 ;;""", namespace)
    local = nsGet(namespace, "/HELLO")
    debug(namespace, str(local))
    assert len(lnsVars(local)) == 1

def test_vm_6():
    namespace = nsCreate()
    namespace = logInit(namespace, 'DEBUG')
    namespace = vmNew(namespace)
    namespace = parser("""[/HELLO> Answer <- 42 ;;""", namespace)
    local = nsGet(namespace, "/HELLO")
    debug(namespace, str(local))
    assert len(lnsVars(local, is_internal=True)) == 4

def test_vm_7():
    namespace = nsCreate()
    namespace = logInit(namespace, 'DEBUG')
    namespace = vmNew(namespace)
    namespace = parser("""[/HELLO> Answer <- 42 ;;""", namespace)
    assert nsGet(namespace, "/config/main.path")[0] == "Main"

def test_vm_8():
    namespace = nsCreate()
    namespace = logInit(namespace, 'DEBUG')
    namespace = vmNew(namespace)
    namespace = parser("""[/HELLO> Answer <- 42 ;;""", namespace)
    assert nsGet(namespace, "/config/pipes.path")[0] == "/pipes"

def test_vm_9():
    namespace = nsCreate()
    namespace = logInit(namespace, 'DEBUG')
    namespace = vmNew(namespace)
    namespace = vmConfig(namespace, answer = 42)
    namespace = parser("""[/HELLO> Answer <- 42 ;;""", namespace)
    assert nsGet(namespace, "/config/answer") == 42

def test_vm_10():
    namespace = nsCreate()
    namespace = logInit(namespace, 'DEBUG')
    namespace = vmNew(namespace)
    namespace = vmConfig(namespace, answer = 42)
    nsSet(namespace, "/templates/answer", "{{ answer }}")
    namespace = parser("""[/HELLO> Answer <- 42 ;;""", namespace)
    assert vmTemplateGenerate(namespace, "answer") == "42"

def test_vm_11():
    namespace = nsCreate()
    namespace = logInit(namespace, 'DEBUG')
    namespace = vmNew(namespace)
    namespace = vmConfig(namespace, answer = 42)
    vmRtSet(namespace, "answer", 42)
    namespace = parser("""[/HELLO> Answer <- 42 ;;""", namespace)
    assert vmRtGet(namespace, "answer") == 42
