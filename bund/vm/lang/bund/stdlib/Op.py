from bund.vm.error import vmError
from bund.library.data import dataValue, dataIsType, dataSetType, copyKW, dataType, dataTypeClass
from bund.vm.vm import vmPeek, vmPull, vmLang, vmGet, vmPush, vmArguments


INTERFACE = {}
OPTIONS={'expand': True}
NAME = "Op"

def actually_plus(namespace, **kw):
    args = vmArguments(namespace, **kw)
    if len(args) == 0:
        return namespace
    args_type = dataTypeClass(args[0])
    if args_type is int:
        c = 0
    elif args_type is float:
        c = 0.0
    elif args_type is str:
        c = ""
    for e in args:
        c += dataValue(e)
    vmPush(namespace, c)
    return namespace

INTERFACE["+"] = actually_plus
