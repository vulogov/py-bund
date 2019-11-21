from bund.library.ns import *
from bund.library.data import *
from bund.library.log import *

def vmConfigNew(namespace, **kw):
    """ Create default config for the (usually) new VM """
    nsSet(namespace, "/config/main.path", ["Main", "/bin/Main"])
    nsSet(namespace, "/config/path", ["/bin", "/custom"])
    nsSet(namespace, "/config/pipes.path", ["/pipes"])
    nsSet(namespace, "/config/templates.path", ["/templates"])
    nsSet(namespace, "/config/templates.namespace", ["/config", "/sys", "/sys/runtime"])
    namespace = vmConfig(namespace, **kw)
    return namespace

def vmConfig(namespace, **kw):
    for k in kw:
        debug(namespace, "Config: {} = {}".format(k, kw[k]))
        nsSet(namespace, "/config/{}".format(k), kw[k])
    return namespace

def vmConfigGet(namespace, name, default):
    return nsGet(namespace, "/config/{}".format(name), default)
