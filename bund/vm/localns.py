import re

def lnsIs(namespace, **kw):
    if namespace is None or isinstance(namespace, dict) is not True:
        return False
    return namespace.get('__namespace__', False)

def lnsUUID(namespace, **kw):
    if namespace is None or isinstance(namespace, dict) is not True:
        return None
    return namespace.get('__id__', None)

def lnsVars(namespace, **kw):
    is_internal = kw.get('is_internal', False)
    res = []
    for k in namespace:
        if is_internal is True:
            res.append(k)
        elif is_internal is False and re.match(r"\_\_(.*)$", k) is None:
            res.append(k)
        else:
            continue
    return res

def lnsGet(namespace, name, **kw):
    v = lnsVars(namespace, **kw)
    if name in v:
        return namespace.get(name)
    return None
