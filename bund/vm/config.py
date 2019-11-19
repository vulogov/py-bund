from bund.library.ns import *
from bund.library.data import *

def vmConfigNew(namespace, **kw):
    """ Create default config for the (usually) new VM """
    nsSet(namespace, "/config/main.path", ["Main", "/bin/Main"])
    nsSet(namespace, "/config/pipes.path", ["/pipes"])
    namespace = vmConfig(namespace, **kw)
    return namespace

def vmConfig(namespace, **kw):
    for k in kw:
        nsSet(namespace, f"/config/%(k)s", kw[k])
    return namespace
