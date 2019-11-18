import imp
import sys
from bund.library.ns import *

def vmBuiltinModuleLoad(namespace, mod_name, **kw):
    lang_name = kw.get('lang', 'default')
    b_path = "/sys/%s/builtins" % lang_name
    lang = nsGet(namespace, "/sys/%s" % lang_name, None)
    if lang is None:
        return namespace
    search_path = kw.get('path', sys.path)
    module = imp.find_module(mod_name, search_path)
    if hasattr(module, 'INTERFACE') is False:
        return namespace
    interface = getattr(module, 'INTERFACE')
    if isinstance(interface, dict) is False:
        return namespace
    builtins = nsGet(namespace, b_path, {})
    buitins.update(interface)
    return namespace
