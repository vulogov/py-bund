from bund.grammar.bund_Grammar import grammar
from bund.ast.namespace import parse_namespace
from textx import metamodel_for_language



def parser(code):
    namespace = {}
    global_repo_provider = grammar()
    mm = metamodel_for_language("basicTypes")
    model = mm.model_from_str(code)
    for n in model.n:
        namespace = parse_namespace(namespace, n)
    return namespace
