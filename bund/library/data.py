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

def dataMake(dataobj, **kw):
    res = {}
    res["value"] = dataobj
    res["type"] = type(dataobj)
    res.update(kw)
    return res
    
