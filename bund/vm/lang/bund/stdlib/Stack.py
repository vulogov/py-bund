INTERFACE = {}
OPTIONS={'expand': True}
NAME = "Stack"

from bund.vm.error import vmError
from bund.library.data import dataValue, dataIsType
from bund.vm.vm import vmPeek, vmPull, vmLang, vmGet, vmPush


def globeThrotter_fun(namespace, **kw):
    next =  vmPeek(namespace, **kw)
    if dataIsType(next, str) is True and dataValue(next) == "%":
        vmPull(namespace, **kw)

def stackSize_fun(namespace, **kw):
    lang = vmLang(namespace, **kw)
    local_namespace = vmGet(namespace, lang)
    try:
        size = 0
        for i, e in reversed(list(enumerate(local_namespace['stack'].queue))):
            if dataValue(e) == '%':
                break
            size += 1
    except KeyError:
        vmError(namespace, msg="No stack in local namespace")
        return
    vmPush(namespace, size)

def stackNoop(namespace):
    return


globeThrotter_fun_stack = True
stackSize_fun_stack = True


INTERFACE["==>"] = globeThrotter_fun
INTERFACE["==?"] = stackSize_fun
INTERFACE["NOOP"] = stackNoop
