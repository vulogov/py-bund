from bund.vm.error import vmError
from bund.library.data import dataValue, dataIsType, dataSetType, copyKW
from bund.vm.vm import vmPeek, vmPull, vmLang, vmGet, vmPush, vmArguments
from bund.vm.eval import vmEvalCtx
from bund.grammar.internal import internalMake


INTERFACE = {}
OPTIONS={'expand': True}
NAME = "Functional"

def actually_lambda(namespace, **kw):
    args = vmArguments(namespace)
    _args = []
    for a in args:
        if dataIsType(a, 'REF_TYPE') is True:
            _args.append(a["value"])
        else:
            _args.append(a)
    l = internalMake(namespace, _args, 'LAMBDA_TYPE', **kw)
    _kw = copyKW(kw, raw=True)
    print(10,l,_kw)
    vmPush(namespace, l, **_kw)
    return namespace

def actually_execute(namespace, **kw):
    args = vmArguments(namespace)
    _kw = copyKW(kw)
    for a in args:
        if dataIsType(a, 'LAMBDA_TYPE') is not True:
            continue
        _kw["take_only"] = 'LAMBDA_TYPE'
        vmEvalCtx(namespace, dataValue(a), **_kw)
    return namespace

INTERFACE["lambda"] = actually_lambda
INTERFACE["!!"] = actually_execute
