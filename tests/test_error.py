import sys
import os
import platform
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from bund.ast.parser import parser
from bund.vm.vm import *
from bund.library.ns import *
from bund.library.log import *
from bund.library.data import *
from bund.vm.error import *


def test_error_1():
    err = vmErrorGenerate(msg="Answer %(answer)d", answer=42)
    assert err['msg'] == "Answer 42"

def test_error_2():
    namespace = nsCreate()
    namespace = logInit(namespace, 'DEBUG')
    namespace = vmNew(namespace)
    namespace = parser("""[/HELLO> ;;""", namespace)
    vmError(namespace, msg="Test")
    err = vmPull(namespace)
    assert err['continue'] == False

def test_error_3():
    namespace = nsCreate()
    namespace = logInit(namespace, 'DEBUG')
    namespace = vmNew(namespace)
    namespace = parser("""[/HELLO> ;;""", namespace)
    vmError(namespace, msg="Test")
    err = vmPull(namespace)
    assert err['msg'] == 'Test'

def test_error_4():
    namespace = nsCreate()
    namespace = logInit(namespace, 'DEBUG')
    namespace = vmNew(namespace)
    namespace = parser("""[/HELLO> ;;""", namespace)
    vmError(namespace, msg="Test")
    assert vmContinue(namespace) == False

def test_error_5():
    namespace = nsCreate()
    namespace = logInit(namespace, 'DEBUG')
    namespace = vmNew(namespace)
    namespace = parser("""[/HELLO> ;;""", namespace)
    vmError(namespace, msg="Test")
    def handler(namespace, err):
        vmPush(namespace, 42)
        return namespace
    vmErrorClear(namespace, handlers=[handler,])
    data = vmPull(namespace)
    assert dataValue(data) == 42
