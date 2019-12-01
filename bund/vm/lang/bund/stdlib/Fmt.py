import time
import pprint
from bund.vm.vm import vmPush, vmPull, vmArguments
from bund.library.data import *
from bund.vm.error import vmError
from bund.library.ns import *
from bund.library.data import dataMake
from bund.ast.value import parse_value

INTERFACE = {}
OPTIONS={'expand': False}
NAME = "Fmt"

def actual_print(namespace):
    data = vmArguments(namespace)
    if data is not None:
        for a in data:
            pprint.pprint(dataValue(a))
    return namespace

def actual_println(namespace):
    data = vmArguments(namespace)
    if data is not None:
        for a in data:
            print(dataValue(a))
            print('\n')
    return namespace

actual_last_stack = True
def actual_last(namespace):
    data = vmPull(namespace)
    if data is not None:
        pprint.pprint(dataValue(data))


INTERFACE["print"] = actual_print
INTERFACE["println"] = actual_print
INTERFACE["printlast"] = actual_last
