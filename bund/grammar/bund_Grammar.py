__doc__ = """
Module docstring
"""
from textx import metamodel_from_str
from textx import clear_language_registrations
from textx import register_language
from bund.grammar.basicTypes import basic_Types
import textx.scoping.providers as scoping_providers
import textx.scoping as scoping
import textx.scoping.tools as tools
import textx.exceptions

GLOBAL_REPO = scoping.GlobalModelRepository()
GLOBAL_REPO_PROVIDER = scoping_providers.PlainNameGlobalRepo()


def getProviders():
    """Returns languale reposittory and reference to provider """
    global GLOBAL_REPO, GLOBAL_REPO_PROVIDER
    return (GLOBAL_REPO, GLOBAL_REPO_PROVIDER)

def get_basic_Metamodel():
    GLOBAL_REPO, GLOBAL_REPO_PROVIDER = getProviders()
    mm = metamodel_from_str(basic_Types, global_repository=GLOBAL_REPO)
    mm.register_scope_providers({'*.*': GLOBAL_REPO_PROVIDER})
    return mm

def grammar():
    clear_language_registrations()
    register_language('basicTypes',
                      pattern="*.bund",
                      metamodel=get_basic_Metamodel)
    return GLOBAL_REPO_PROVIDER
