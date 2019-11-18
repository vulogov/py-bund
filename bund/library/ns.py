from dpath.util import get as dpath_get
from dpath.util import new as dpath_new
from dpath.util import set as dpath_set


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
