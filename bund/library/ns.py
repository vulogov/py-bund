import uuid
from dpath.util import get as dpath_get
from dpath.util import new as dpath_new
from dpath.util import set as dpath_set

def nsCreate(**kw):
    namespace = {}
    nsSet(namespace, '__main__', {})
    nsSet(namespace, '__namespace__', True)
    nsSet(namespace, '/bin', {})
    nsSet(namespace, '/config', {})
    nsSet(namespace, '/tmp', {})
    nsSet(namespace, '/sys', {})
    nsSet(namespace, '/sys/log', {})
    nsSet(namespace, '/conditions', {})
    nsSet(namespace, '/config/compiled', False)
    nsSet(namespace, "/sys/log/ready", False)
    nsSet(namespace, "/sys/id", str(uuid.uuid4()))
    return namespace

def nsNew(namespace, name):
    try:
        res =  dpath_get(namespace, name)
    except KeyError:
        dpath_new(namespace, name, {'__namespace__': True})
        res = dpath_get(namespace, name)
    return res

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
