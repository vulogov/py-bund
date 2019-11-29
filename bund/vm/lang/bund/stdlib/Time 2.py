import time
from bund.vm.vm import vmPush, vmPull
from bund.vm.error import vmError
from bund.library.ns import *
from bund.library.data import dataMake
from bund.ast.value import parse_value

INTERFACE = {}
OPTIONS={'expand': False}
NAME = "Time"

def Now(namespace):
    vmPush(namespace, time.time())
    return namespace

INTERFACE["Now"] = Now
