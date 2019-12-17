from bund.vm.vm import vmGet, vmPull, vmPush, vmLang, vmStack, vmArgumentsClear
from bund.vm.vm import vmUnargument, vmArguments
from bund.vm.error import vmError
from bund.vm.builtins import vmBuiltinGet
from bund.vm.localns import *
from bund.vm.config import *
from bund.library.ns import *
from bund.library.data import *


def vmLocateSymbol(namespace, sym, **kw):
    is_nsid = isNSID(namespace, sym)
    if is_nsid is True:
        res = nsGet(namespace, sym, None)
        if res is not None and isinstance(res, dict):
            return res
    localns = kw.get("ns", None)
    if localns is not None:
        localns = nsGet(namespace, localns)
    if isinstance(localns, dict) is False:
        localns = nsGet(namespace, "__main__")
    if localns is not None and isinstance(localns, dict) is True:
        res = lnsGet(localns, sym, **kw)
        if res is not None:
            return res
    if is_nsid is False:
        search_path = vmConfigGet(namespace, "path", ["/bin", "/custom"])
        for s in search_path:
            res = nsGet(namespace, "{}/{}".format(s, sym))
            if res is not None:
                return res
    return vmBuiltinGet(namespace, sym, **kw)

def vmEvalString(namespace, w, **kw):
    if dataValue(w) == ";":
        vmStack(namespace, **kw)
        _fun = vmPull(namespace, **kw)
        if dataIsType(_fun, 'PRELIMENARY_EXECUTE_TYPE') is not True:
            vmPush(namespace, _fun, raw=True)
            vmUnargument(namespace, **kw)
            vmPush(namespace, w, raw=True)
            return namespace
        else:
            _fun = dataValue(_fun).name
    else:
        _fun = dataValue(w)
    fun = vmLocateSymbol(namespace, _fun, **kw)
    print(34,fun, _fun)
    if fun is None:
        vmPush(namespace, w, raw=True)
        return namespace
    if dataIsType(fun, 'builtin_function') is True or dataIsType(fun, 'LAMBDA_TYPE'):
        if fun.get('keep_stack', False) is not True:
            vmStack(namespace, **kw)
            vmArgumentsClear(namespace, **kw)
        dataValue(fun)(namespace)
    else:
        vmPush(namespace, w, raw=True)
    return namespace


def vmEvalCtx(namespace, ctx, **kw):
    for w in ctx:
        if isinstance(w, dict) is not True:
            vmError(namespace, msg="Corrupted context. Unexpected element", elem=w)
            break
        if dataIsType(w, int):
            vmPush(namespace, w, raw=True)
        elif dataIsType(w, float):
            vmPush(namespace, w, raw=True)
        elif dataIsType(w, str):
            vmEvalString(namespace, w, **kw)
        elif dataIsType(w, 'LAMBDA_TYPE'):
            vmPush(namespace, '%')
            vmEvalCtx(namespace, dataValue(w), **kw)
        else:
            vmPush(namespace, w, raw=True)
    return namespace

def vmEval(namespace, path, **kw):
    kw["ns"] = path
    lang = vmLang(namespace, **kw)
    local_ns = nsGet(namespace, path)
    if local_ns is None or isinstance(local_ns, dict) is not True:
        return None
    script = local_ns.get("script", None)
    if script is not None:
        return vmEvalCtx(namespace, script, **kw)
    if dataType(local_ns) != 'LAMBDA_TYPE':
        return namespace
    words = local_ns.get("value", None)
    return vmEvalCtx(namespace, script, **kw)
