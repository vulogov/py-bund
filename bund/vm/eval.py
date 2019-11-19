from bund.vm.vm import vmGet, vmPull, vmPush
from bund.vm.error import vmError
from bund.library.ns import *

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
