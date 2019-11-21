from bund.vm.vm import vmGet, vmPull, vmPush
from bund.vm.error import vmError
from bund.vm.error import vmBuiltinGet
from bund.vm.localns import *
from bund.vm.config import *
from bund.library.ns import *

def vmLocateSymbol(namespace, sym, **kw):
    if isNSID(sym) is True:
        return nsGet(namespace, sym, None)
    localns = kw.get("ns", None)
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




def vmEval(namespace, _path=None, **kw):
    lang = kw.get('lang', 'bund')
    starting_point = kw.get('eval', None)
    if starting_point is None:
        if _path is not None:
            path = _path
        elif kw.get("path", None) is not None:
            path = kw.get("path", None)
        else:
            vmError(msg="Unidentified starting point for eval")
            return namespace
        starting_point = nsGet(namespace, path)
        if starting_point is None:
            vmError(msg="Starting point for eval does not exists")
            return namespace
    sys_namespace = vmGet(namespace, lang)
