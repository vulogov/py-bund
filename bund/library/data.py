import time
import copy
class builtin_module(object): pass
class builtin_function(object): pass

class namespace_type: pass

def isContinue(data):
    if data is None:
        return True
    if isinstance(data, dict) is not True:
        return True
    return data.get("continue", True)

def dataValue(data):
    if data is None:
        return None
    if isinstance(data, dict) is not True:
        return None
    if dataIsType(data, 'REF_TYPE') is True:
        val = data["value"]["value"]
    else:
        val = data.get('value', None)
    return val

def dataIsType(data, typeclass):
    if data is None:
        return None
    if isinstance(data, dict) is not True:
        return None
    if '__namespace__' in data and data['__namespace__'] is True:
        return  namespace_type
    d = data.get('type', None)
    if isinstance(typeclass, str) is True and isinstance(d, str) is True:
        return d == typeclass
    elif isinstance(typeclass, str) is True and isinstance(d, object) is True:
        return d.__name__ == typeclass
    else:
        return data.get('type', None) == typeclass

def dataType(data):
    return dataTypeClass(data).__name__

def dataTypeClass(data):
    if data is None:
        return None
    if isinstance(data, dict) is not True:
        return None
    if '__namespace__' in data and data['__namespace__'] is True:
        return 'namespace_type'
    typeclass = data.get('type', type(None))
    return typeclass

def dataSetType(data, typeclass):
    if data is None:
        return None
    if isinstance(data, dict) is not True:
        return None
    if "type" in data:
        data["type"] = typeclass
    return data

def dataMake(dataobj, **kw):
    res = {}
    res["value"] = dataobj
    res["type"] = kw.get("typeclass", type(dataobj))
    res["msg"] = ""
    res["continue"] = True
    res["stamp"] = time.time()
    res.update(kw)
    return res

def dataUpdate(dataval, **kw):
    dataval.update(kw)
    return dataval

def copyKW(_kw, **kw):
    new_kw = copy.copy(_kw)
    new_kw.update(kw)
    return new_kw
