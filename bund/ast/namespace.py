from bund.ast.assignments import pars_eassignments
from dpath.util import get as dpath_get
from dpath.util import new as dpath_new


def parse_namespace(namespace, n):
    try:
        local_namespace = dpath_get(namespace, n.name)
    except KeyError:
        local_namespace = dpath_new(namespace, n.name, {})
    namespace = parse_assignments(namespace, n)
    for n in n.ns:
        namespace = parse_namespace(namespace, n)
    return namespace
