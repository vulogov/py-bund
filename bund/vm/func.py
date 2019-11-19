from bund.library.ns import *

def vmArgs(namespace, **kw):
    lang = kw.get('lang', 'bund')
    local_namespace = vmGet(namespace, lang)
    return local_namespace['arguments']

def vmArgsAdd(namespace, *objs, **kw):
    args = vmArgs(namespace, **kw)
    args += objs
    return namespace

def vmArgsSet(namespace, *objs, **kw):
    args = vmArgs(namespace, **kw)
    args = list(objs)
    return namespace

def vmArgsClear(namespace, *objs, **kw):
    return vmArgsSet(namespace, **kw)
