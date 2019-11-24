import sys
import importlib
from bund.vm.config import vmConfigGet

def pyImport(namespace, *mod_names, **kw):
    sys.path = vmConfigGet(namespace, "builtinmodules.path", sys.path)
    modules = namespace["sys"]["modules"]
    if isinstance(modules, list) is not True:
        return []
    res = []
    for m in mod_names:
        try:
            mod = importlib.import_module(m)
        except ModuleNotFoundError:
            continue
        if mod not in res:
            res.append(mod)
        if m not in modules:
            modules.append(m)
    return res
