import bund.ast.value


def LAMBDA_TYPE(data):
    res = {}
    res['value'] = []
    for w in data.words:
        res['value'].append(parse_value(w))
    return res

def REF_TYPE(data):
    res = {}
    res['value'] = parse_value(data.data)
    return res

def KV_TYPE(data):
    res = {}
    res['value'] = {data.name : parse_value(data.data)}
    return res

def CURRY_TYPE(data):
    res = {}
    res['value'] = (data.name, parse_value(data.value))
    return res

def PRELIMENARY_EXECUTE_TYPE(data):
    res = {}
    res['value'] = parse_value(data.name)
    return res

def LIST_TYPE(data):
    res = {}
    c = 0
    for d in data.data:
        if isinstance(d, object) and d.__class__.__name__ == 'KV_TYPE':
            key = d.name
            value = d.value
        else:
            key = c
            value = d
        c += 1
        res[key] = parse_value(value)
    return {'value': res, 'type':data.__class__}


def parse_value(data):
    if isinstance(data, int):
        res = {"value": data, "type": int}
    elif isinstance(data, float):
        res = {"value": data, "type": float}
    elif isinstance(data, str):
        res = {"value": data, "type": str}
    elif isinstance(data, object):
        if hasattr(bund.ast.value, data.__class__.__name__) is True:
            f = getattr(bund.ast.value, data.__class__.__name__)
            _res = f(data)
            _res['type'] = data.__class__
            res = _res
        else:
            res = {'value': data, 'type':data.__class__}
    else:
        res = {"value": data, "type": lambda x: x is None}
    res["continue"] = True
    res["msg"] = ""
    return res
