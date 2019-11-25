from bund.grammar.bund_Grammar import grammar
from bund.ast.namespace import parse_namespace
from bund.ast.value import parse_value
from textx import metamodel_for_language
from dpath.util import get as dpath_get
from dpath.util import new as dpath_new
from bund.ast.assignments import INTERFACE as assignments_INTERFACE
from bund.library.log import *


def parser(code, _namespace=None):
    if _namespace is None:
        namespace = {}
        dpath_new(namespace, "__main__", {})
        dpath_new(namespace, "__script__", [])
        dpath_new(namespace, "__namespace__", True)
        dpath_new(namespace, "/bin", {})
        dpath_new(namespace, "/config", {'compiled':False})
        dpath_new(namespace, "/tmp", {})
        dpath_new(namespace, "/sys", {})
        dpath_new(namespace, "/conditions", {})
    else:
        namespace = _namespace
    if "metamodel" not in namespace["sys"]:
        dpath_new(namespace, "/sys/is.metamodel", parserSetup(namespace))
    return parseIn(namespace, code)

def parserSetup(namespace):
    parsers = {}
    parsers.update(assignments_INTERFACE)
    global_repo_provider = grammar()
    mm = metamodel_for_language("basicTypes")
    dpath_new(namespace, "/sys/metamodel", mm)
    dpath_new(namespace, "/sys/parsers", parsers)
    dpath_new(namespace, "/sys/global_repo_provider", global_repo_provider)
    return True

def parseIn(namespace, code):
    mm = dpath_get(namespace, "/sys/metamodel")
    parsers = dpath_get(namespace, "/sys/parsers")
    model = mm.model_from_str(code)
    debug(namespace, "Scanning '__main__' variables")
    for a in model.a:
        name = a.__class__.__name__
        if name in parsers:
            namespace = parsers[name](namespace, parsers, model, assign=a, ns="__main__")
    for n in model.n:
        namespace = parse_namespace(namespace, parsers, n)
    namespace = parseD(namespace, model.d)
    return namespace

def parseD(namespace, data):
    res = dpath_get(namespace, "__script__")
    for d in data:
        val = parse_value(d)
        res.append(val)
        if val["continue"] is not True:
            return namespace
    return namespace
