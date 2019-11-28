from bund.vm.vm import vmGet, vmPull, vmPush, vmLang
from bund.vm.error import vmError
from bund.vm.builtins import vmBuiltinGet
from bund.vm.localns import *
from bund.vm.config import *
from bund.library.ns import *
from bund.library.data import *


def vmLocateSymbol(namespace, sym, **kw):
    if isNSID(sym) is True:
        return nsGet(namespace, sym, None)
    localns = kw.get("ns", None)
    if localns is not None and isinstance(localns, dict) is True:
        res = lnsGet(localns, sym, **kw)
        if res is not None:
            return res
    localns = nsGet(namespace, "__main__")
    if localns is not None and isinstance(localns, dict) is True:
        res = lnsGet(localns, sym, **kw)
        if res is not None:
            return res
    search_path = vmConfigGet(namespace, "/config/path", ["/bin", "/custom"])
    for s in search_path:
        res = nsGet(namespace, "{}/{}".format(s, sym))
        if res is not None:
            return res
    return vmBuiltinGet(namespace, sym, **kw)

def vmEvalString(namespace, w):
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
            vmEvalString(namespace, w)
        else:
            vmPush(namespace, w, raw=True)
    return namespace

def vmEval(namespace, path, **kw):
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
