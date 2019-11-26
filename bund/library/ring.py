import collections
from bund.library.data import *
from dpath.util import get as dpath_get
from dpath.util import new as dpath_new
from dpath.util import set as dpath_set

class ring_type: pass

def ringNew(max_size = None, *args, **kw):
    data = {'type': ring_type, 'continue': True, 'msg':'', 'uniq':False}
    dpath_new(data, "max_size", 0)
    data.update(kw)
    dpath_new(data, "value", collections.deque(args, max_size))
    return data

def ringAdd(_ring, *data):
    if dataIsType(_ring, ring_type) is not True:
        return False
    if dpath_get(_ring, 'uniq') is True:
        try:
            dataValue(_ring)
            return False
        except ValueError:
            pass
    if dpath_get(_ring, "max_size") is not None:
        if dpath_get(_ring, "max_size") < len(dataValue(_ring))+len(data):
            for i in data:
                try:
                    dataValue(_ring).popleft()
                except IndexError:
                    break
    data = list(data)
    data.reverse()
    dataValue(_ring).extendleft(data)
    return True

def ringTip(_ring):
    if dataIsType(_ring, ring_type) is not True:
        return None
    return dataValue(_ring)[0]

def ringLeft(_ring):
    if dataIsType(_ring, ring_type) is not True:
        return None
    return dataValue(_ring)[-1]

def ringRight(_ring):
    if dataIsType(_ring, ring_type) is not True:
        return None
    return dataValue(_ring)[1]

def ringTick(_ring, n=1):
    if dataIsType(_ring, ring_type) is not True:
        return None
    return dataValue(_ring).rotate(-n)

def ringPop(_ring):
    if dataIsType(_ring, ring_type) is not True:
        return None
    return dataValue(_ring).popleft()

def ringFind(_ring, val):
    if dataIsType(_ring, ring_type) is not True:
        return None
    try:
        ix = dataValue(_ring).index(val)
        dataValue(_ring).rotate(-ix)
        return dataValue(_ring)[0]
    except ValueError:
        pass
    return None
