import time
from bund.vm.vm import vmPush, vmPull
from bund.vm.error import vmError
from bund.library.ns import *
from bund.library.data import dataMake
from bund.ast.value import parse_value

INTERFACE = {}
OPTIONS={'expand': False}
NAME = "Fmt"

def actual_print(namespace):
    data = vmPull(namespace)
    if data is not None:
        print(dataValue(data))
    return namespace

INTERFACE["print"] = actual_print
