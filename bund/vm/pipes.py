from bund.library.ns import *
from bund.library.data import *
from bund.vm.pipe import *
from bund.vm.python import pyImport

class pipe: pass

def vmPipesDefaultInit(namespace, **kw):

    return namespace

def vmPipesMake(namespace, **kw):
    pipedef = vmPipesConfigure(namespace, **kw)
    if pipedef is None:
        return None
    params = {}
    params['typeclass'] = pipe
    p = dataMake()
    return p

def vmPipesConfigure(namespace, **kw):
    name = kw.get("name", None)
    if name is None:
        return None
    ptype = kw.get("type", "fifo")
    pname = "bund.vm.pipe.{}".format(ptype)
    _pmod = pyImport(namespace, _pname)
    if len(_pmod) == 0:
        return None
