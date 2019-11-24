import sys
from bund.library.ns import *
from bund.library.data import *
from bund.library.log import *

def vmConfigNew(namespace, **kw):
    """ Create default config for the (usually) new VM """
    nsSet(namespace, "/config/bootstrap", ["bootstrap", "/bin/bootstrap"])
    nsSet(namespace, "/config/main.path", ["Main", "/bin/Main"])
    nsSet(namespace, "/config/path", ["/bin", "/custom"])
    nsSet(namespace, "/config/pipes.path", ["/pipes"])
    nsSet(namespace, "/config/templates.path", ["/templates"])
    nsSet(namespace, "/config/templates.namespace", ["/config", "/sys", "/sys/runtime"])
    nsSet(namespace, "/config/scripts.autorun", False)
    nsSet(namespace, "/config/builtinmodules.path", sys.path)
    namespace = vmConfig(namespace, **kw)
    return namespace

def vmConfig(namespace, **kw):
    for k in kw:
        debug(namespace, "Config: {} = {}".format(k, kw[k]))
        vmConfigSet(namespace, k, kw[k])
    return namespace

def vmConfigGet(namespace, name, default=None):
    return nsGet(namespace, "/config/{}".format(name), default)

def vmConfigSet(namespace, name, value):
    nsSet(namespace, "/config/{}".format(name), value)
    return namespace

def vmConfigAppend(namespace, name, *args):
    data = vmConfigGet(namespace, name, None)
    if data is None:
        return namespace
    if isinstance(data, list) is not True:
        return namespace
    data += list(args)
    return namespace

def vmConfigFlip(namespace, name):
    data = vmConfigGet(namespace, name, None)
    if data is None:
        return namespace
    if isinstance(data, bool) is not True:
        return namespace
    vmConfig(namespace, name=not data)
