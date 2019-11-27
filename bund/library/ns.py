import uuid
import time
from dpath.util import get as dpath_get
from dpath.util import new as dpath_new
from dpath.util import set as dpath_set

def nsCreate(**kw):
    namespace = {}
    nsNew(namespace, '__main__')
    nsNew(namespace, '__script__')
    nsSet(namespace, '__namespace__', True)
    nsNew(namespace, '/bin')
    nsNew(namespace, '/custom')
    nsNew(namespace, '/scripts')
    nsNew(namespace, '/config')
    nsNew(namespace, '/pipes')
    nsNew(namespace, '/tmp')
    nsNew(namespace, '/sys')
    nsNew(namespace, '/sys/log')
    nsNew(namespace, '/sys/pipes')
    nsNew(namespace, '/sys/runtime')
    nsNew(namespace, '/conditions')
    nsNew(namespace, '/templates')
    nsSet(namespace, '/config/compiled', False)
    nsSet(namespace, "/sys/log/ready", False)
    nsSet(namespace, "/sys/id", str(uuid.uuid4()))
    namespace.update(kw)
    return namespace

def nsNew(namespace, name):
    ns = nsSet(namespace, name, {'__namespace__': True})
    nsSet(namespace, "%s/__id__" % name, str(uuid.uuid4()))
    nsSet(namespace, "%s/__stamp__" % name, time.time())
    nsSet(namespace, "%s/__name__" % name, name)
    return ns

def nsSet(namespace, name, default=None):
    try:
        dpath_get(namespace, name)
        dpath_set(namespace, name, default)
    except KeyError:
        dpath_new(namespace, name, default)
    return default

def nsGet(namespace, name, default=None):
    try:
        res =  dpath_get(namespace, name)
    except KeyError:
        res = default
    return res

def isNSID(namespace, sym):
    if isinstance(sym, str) is False:
        return False
    return sym[0] == "/"

def isNamespace(namespace, name):
    return nsGet(namespace, "{}/__namespace__".format(name), False)

def nsMain(namespace):
    return nsGet(namespace, "__main__")

def nsScript(namespace):
    return nsGet(namespace, "__script__")
