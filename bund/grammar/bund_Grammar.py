from textx import metamodel_from_str
from textx import clear_language_registrations
from textx import register_language
from bund.grammar.basicTypes import basic_Types
from bund.grammar.namespaceTypes import namespace_Types
import textx.scoping.providers as scoping_providers
import textx.scoping as scoping
import textx.scoping.tools as tools
import textx.exceptions


bund_Grammar = """
reference basicTypes as base
reference namespaceTypes as name
Bund:
    namespaces *= name.NamespaceDef
;
"""

GLOBAL_REPO = scoping.GlobalModelRepository()
GLOBAL_REPO_PROVIDER = scoping_providers.PlainNameGlobalRepo()


def getProviders():
    global GLOBAL_REPO, GLOBAL_REPO_PROVIDER
    return (GLOBAL_REPO, GLOBAL_REPO_PROVIDER)


def get_basic_Metamodel():
    GLOBAL_REPO, GLOBAL_REPO_PROVIDER = getProviders()
    mm = metamodel_from_str(basic_Types, global_repository=GLOBAL_REPO)
    mm.register_scope_providers({'*.*': GLOBAL_REPO_PROVIDER})
    return mm


def get_namespace_Metamodel():
    GLOBAL_REPO, GLOBAL_REPO_PROVIDER = getProviders()
    mm = metamodel_from_str(namespace_Types, global_repository=GLOBAL_REPO)
    mm.register_scope_providers({'*.*': GLOBAL_REPO_PROVIDER})
    return mm


def get_bund_Metamodel():
    global GLOBAL_REPO, GLOBAL_REPO_PROVIDER
    mm = metamodel_from_str(bund_Grammar, global_repository=GLOBAL_REPO)
    mm.register_scope_providers({'*.*': GLOBAL_REPO_PROVIDER})
    return mm


def grammar():
    clear_language_registrations()
    register_language('basicTypes',
                      pattern="*.base",
                      metamodel=get_basic_Metamodel)
    register_language('namespaceTypes',
                      pattern="*.name",
                      metamodel=get_namespace_Metamodel)
    register_language('bund_Grammar',
                      pattern="*.bund",
                      metamodel=get_bund_Metamodel)
    return GLOBAL_REPO_PROVIDER
