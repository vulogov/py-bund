import types
from bund.library.ns import *
from bund.library.data import *
from bund.vm.pipe import *
from bund.vm.python import pyImport


def vmPipesDefaultInit(namespace, **kw):
    vmPipeMake(namespace, "clock", type="clock")
    vmPipeMake(namespace, "random", type="random")
    return namespace

def vmPipeMake(namespace, name=None, **kw):
    if name is None:
        _name = kw.get("name", None)
    else:
        _name = name
    if _name is None:
        return None
    pipedef = vmPipeConfigure(namespace, _name, **kw)
    if pipedef is None:
        return None
    nsSet(namespace, "/pipes/{}".format(_name), pipedef)
    return namespace

def vmPipeConfigure(namespace, name, **kw):
    if name is None:
        return None
    ptype = kw.get("type", "fifo")
    pname = "bund.vm.pipe.{}".format(ptype)
    _pmod = pyImport(namespace, pname)
    if len(_pmod) == 0:
        return None
    if hasattr(_pmod[0], "init") is not True:
        return None
    return getattr(_pmod[0], "init")(namespace, name, **kw)

def vmPipeGet(namespace, name):
    pipe = nsGet(namespace, "/pipes/{}".format(name), None)
    if pipe is None:
        return None
    return pipe

def pipeCan(pipeObj, key):
    if key in pipeObj:
        if pipeObj[key] is not None and isinstance(pipeObj[key], types.FunctionType):
            return True
    return False

def pipeCanRead(pipeObj):
    return pipeCan(pipeObj, "read")

def pipeCanWrite(pipeObj):
    return pipeCan(pipeObj, "write")

def pipeCanSeek(pipeObj):
    return pipeCan(pipeObj, "seek")

def pipeCanTell(pipeObj):
    return pipeCan(pipeObj, "tell")

def pipeCanClose(pipeObj):
    return pipeCan(pipeObj, "close")

def pipeRead(namespace, pipeObj, **kw):
    if pipeCanRead(pipeObj) is True:
        return pipeObj["read"](namespace, pipeObj, **kw)
    return None

def pipeWrite(namespace, pipeObj, *data, **kw):
    if pipeCanWrite(pipeObj) is True:
        is_raw = kw.get("raw", False)
        for d in data:
            if is_raw is False:
                _data = dataMake(d, **kw)
            else:
                _data = d
            pipeObj["write"](namespace, pipeObj, _data, **kw)
    return None

def pipeSeek(namespace, pipeObj, **kw):
    if pipeCanSeek(pipeObj) is True:
        return pipeObj["seek"](namespace, pipeObj, **kw)
    return None

def pipeTell(namespace, pipeObj):
    if pipeCanTell(pipeObj) is True:
        return pipeObj["tell"](namespace, pipeObj)
    return None

def pipeClose(namespace, pipeObj):
    if pipeCanClose(pipeObj) is True:
        return pipeObj["close"](namespace, pipeObj)
    return None
