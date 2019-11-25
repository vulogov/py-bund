import sys
from bund.vm.vm import vmLang, vmSys
from bund.vm.config import vmConfigGet
from bund.vm.python import pyImport
from bund.library.ns import *
from bund.library.data import *



def vmBuiltinModuleLoad(namespace, mod_name, **kw):
    lang_name = vmLang(namespace, **kw)
    b_path = "/sys/{}/builtins".format(lang_name)
    lang = nsGet(namespace, "/sys/%s" % lang_name, None)
    if lang is None:
        return namespace
    search_path = kw.get('path', None)
    if search_path is None:
        search_path = vmConfigGet(namespace, "builtinmodules.path", sys.path)
    modules = pyImport(namespace, mod_name)
    if len(modules) == 0:
        return namespace
    module = modules[0]
    if hasattr(module, 'INTERFACE') is False:
        return namespace
    if hasattr(module, 'NAME') is False:
        return namespace
    if hasattr(module, 'OPTIONS') is False:
        return namespace
    interface = getattr(module, 'INTERFACE')
    module_name = getattr(module, 'NAME')
    module_options = getattr(module, 'OPTIONS')
    if isinstance(interface, dict) is False:
        return namespace
    if isinstance(module_options, dict) is False:
        return namespace
    if isinstance(module_name, str) is False:
        return namespace
    builtins = nsGet(namespace, b_path, {})
    if module_name in builtins:
        del builtins[module_name]
    if module_options.get('expand', False) is False:
        builtins[module_name] = interface
    else:
        for f in interface:
            builtins[f] = interface[f]
    return namespace

def vmBuiltinModule(namespace, mod_name, **kw):
    lang_name = vmLang(namespace, **kw)
    m_path = "bund.vm.lang.{}.stdlib.{}".format(lang_name, mod_name)
    return vmBuiltinModuleLoad(namespace, m_path, **kw)

def vmBuiltinGet(namespace, name, **kw):
    if isinstance(name, str) is not True:
        return None
    builtins = vmSys(namespace, "builtins")
    if name[0] == "/":
        mod_name = name.split("/")[1:]
    else:
        mod_name = name.split(".")
    if len(mod_name) == 1:
        if mod_name[0] in builtins:
            if isinstance(builtins[mod_name[0]], dict) is True:
                return dataMake(builtins[mod_name[0]], typeclass=builtin_module)
            else:
                return dataMake(builtins[mod_name[0]], typeclass=builtin_function)
    if len(mod_name) == 2:
        if mod_name[0] in builtins:
            mod = builtins[mod_name[0]]
            if isinstance(mod, dict) is True:
                if mod_name[1] in mod:
                    return dataMake(mod[mod_name[1]], typeclass=builtin_function)
    return None
