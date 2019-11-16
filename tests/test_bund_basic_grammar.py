import pytest
from textx import metamodel_for_language
from bund.grammar.bund_Grammar import grammar


def test_bund_base_grammar_NUMBER():
    global_repo_provider = grammar()
    mm = metamodel_for_language("basicTypes")
    model = mm.model_from_str("ANSWER <- 42")
    model = mm.model_from_str("42 as ANSWER")

def test_bund_base_grammar_STR():
    global_repo_provider = grammar()
    mm = metamodel_for_language("basicTypes")
    model = mm.model_from_str('TEXT <- "Привет, Hello"')
    model = mm.model_from_str('"Hello World" -> Hello')

def test_bund_base_grammar_NUMBER():
    global_repo_provider = grammar()
    mm = metamodel_for_language("basicTypes")
    model = mm.model_from_str("PI is 3.14")
    model = mm.model_from_str("3.14 -> Pi")

def test_bund_base_grammar_LIST():
    global_repo_provider = grammar()
    mm = metamodel_for_language("basicTypes")
    model = mm.model_from_str('LIST <- |1, "Привет", 3.14 |')

def test_bund_base_grammar_ASSIGN():
    global_repo_provider = grammar()
    mm = metamodel_for_language("basicTypes")
    model = mm.model_from_str('LIST <- | { PI  3.14 }, "Hello world!", 42 |')
    model = mm.model_from_str('Kw <- { PI  3.14} ')

def test_bund_base_grammar_LAMBDA():
    global_repo_provider = grammar()
    mm = metamodel_for_language("basicTypes")
    model = mm.model_from_str('runMe <- (42)')

def test_bund_base_grammar_REF():
    global_repo_provider = grammar()
    mm = metamodel_for_language("basicTypes")
    model = mm.model_from_str('refMe <- `42')

def test_bund_base_grammar_CURRY():
    global_repo_provider = grammar()
    mm = metamodel_for_language("basicTypes")
    model = mm.model_from_str('curryMe <- ( runMe . 42 )')

def test_bund_base_grammar_DO():
    global_repo_provider = grammar()
    mm = metamodel_for_language("basicTypes")
    model = mm.model_from_str('doMe <- ( : runMe "Param1" 2 3.14 |5, 6| ; )')
    model = mm.model_from_str("""
    doMe <- ( 1 2 3 runMeFromStack 2 curryMe : curryMe 2 ; )
    """)

def test_bund_base_grammar_NSID():
    global_repo_provider = grammar()
    mm = metamodel_for_language("basicTypes")
    model = mm.model_from_str('doMe <- ( : /RunMe/A/B "With NSID" ; )')