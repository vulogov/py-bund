from dpath.util import get as dpath_get
from dpath.util import new as dpath_new


def parse_namespace(namespace, parsers, n):
    try:
        local_namespace = dpath_get(namespace, n.name)
    except KeyError:
        dpath_new(namespace, n.name, {})
        local_namespace = dpath_get(namespace, n.name)
    for a in n.statements:
        name = a.__class__.__name__
        if name in parsers:
            namespace = parsers[name](namespace, parsers, n, assign=a, ns=n.name)
    for n in n.ns:
        namespace = parse_namespace(namespace, parsers, n)
    return namespace
