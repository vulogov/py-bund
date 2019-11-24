import sys
import importlib
from bund.vm.config import vmConfigGet
from bund.library.data import *

class python_function(object): pass

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

def pyImportFun(namespace, mod_name, *fun_name, **kw):
    mod = pyImport(namespace, mod_name, **kw)
    res = {}
    for m in mod:
        for f in fun_name:
            if hasattr(m, f) is True:
                res[f] = dataMake(getattr(m, f), typeclass=python_function)
    return res
