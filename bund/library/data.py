import time
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
    return data.get('value', None)

def dataIsType(data, typeclass):
    if data is None:
        return None
    if isinstance(data, dict) is not True:
        return None
    if '__namespace__' in data and data['__namespace__'] is True:
        return  namespace_type
    if isinstance(typeclass, str) is True:
        return data.get('type', None).__name__ == typeclass
    else:
        return data.get('type', None) == typeclass

def dataType(data):
    if data is None:
        return None
    if isinstance(data, dict) is not True:
        return None
    if '__namespace__' in data and data['__namespace__'] is True:
        return 'namespace_type'
    typeclass = data.get('type', type(None))
    return typeclass.__name__

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
