import time
from bund.vm.vm import vmGet
from bund.vm.error import vmError
from bund.library.ns import *
from bund.ast.value import parse_value

INTERFACE = {}

def Now(namespace):
    lang = vmGet(namespace)
    if lang is None:
        vmError(namespace, msg="Language not found")
