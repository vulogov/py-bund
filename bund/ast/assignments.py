from dpath.util import get as dpath_get
from dpath.util import new as dpath_new
from bund.ast.value import parse_value
from bund.library.log import *

INTERFACE = {}

def DirectAssignmentDef(namespace, parsers, model, **kw):
    if "ns" in kw and "assign" in kw:
        namespace_name = kw["ns"]
    elif "assign" in kw:
        namespace_name = "__main__"
    else:
        return namespace
    obj = kw["assign"]
    local_namespace = dpath_get(namespace, namespace_name)
    if not local_namespace:
        dpath_new(namespace, namespace_name, {})
        local_namespace = dpath_get(namespace, namespace_name)
    debug(namespace, "%(ns)s : %(name)s = %(data)s", ns=namespace_name, name=obj.name, data=str(obj.data))
    local_namespace[obj.name] = parse_value(obj.data)
    return namespace


INTERFACE["DirectAssignmentDef"] = DirectAssignmentDef
INTERFACE["ReverseAssignmentDef"] = DirectAssignmentDef
