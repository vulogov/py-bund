from bund.grammar.bund_Grammar import grammar
from bund.ast.namespace import parse_namespace
from textx import metamodel_for_language
from dpath.util import get as dpath_get
from dpath.util import new as dpath_new
from bund.ast.assignments import INTERFACE as assignments_INTERFACE
from bund.library.log import *


def parser(code, _namespace=None):
    if _namespace is None:
        namespace = {}
        dpath_new(namespace, "__main__", {})
        dpath_new(namespace, "__namespace__", True)
        dpath_new(namespace, "/bin", {})
        dpath_new(namespace, "/config", {'compiled':False})
        dpath_new(namespace, "/tmp", {})
        dpath_new(namespace, "/sys", {})
        dpath_new(namespace, "/conditions", {})
    else:
        namespace = _namespace
    parsers = {}
    parsers.update(assignments_INTERFACE)
    global_repo_provider = grammar()
    mm = metamodel_for_language("basicTypes")
    model = mm.model_from_str(code)
    for a in model.a:
        name = a.__class__.__name__
        if name in parsers:
            namespace = parsers[name](namespace, parsers, model, assign=a, ns="__main__")
    for n in model.n:
        namespace = parse_namespace(namespace, parsers, n)
    return namespace
