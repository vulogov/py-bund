from bund.library.ns import *


def parse_namespace(namespace, parsers, n):
    local_namespace = nsNew(namespace, n.name)
    for a in n.statements:
        name = a.__class__.__name__
        if name in parsers:
            namespace = parsers[name](namespace, parsers, n, assign=a, ns=n.name)
    for n in n.ns:
        namespace = parse_namespace(namespace, parsers, n)
    return namespace
