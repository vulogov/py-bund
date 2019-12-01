import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from bund.ast.parser import parser

def test_parser1():
    namespace = parser("""[/HELLO> ;;""")
    assert isinstance(namespace["HELLO"], dict)

def test_parser_2():
    namespace = parser("""Pi <- 3.14""")
    assert namespace['__main__']['Pi']['value'] == 3.14

def test_parser_3():
    namespace = parser("""[/HELLO> Pi <- 3.14 ;;""")
    assert namespace['HELLO']['Pi']['value'] == 3.14

def test_parser_3():
    namespace = parser("""[/HELLO> theList <- | 1, 2, 3 | ;;""")
    assert len(namespace['HELLO']['theList']['value']) == 3

def test_parser_4():
    namespace = parser("""[/HELLO> theList <- | 1, 2, 3 | ;;""")
    assert namespace['HELLO']['theList']['value'][0]['value'] == 1

def test_parser_5():
    namespace = parser("""[/HELLO> theKv <- {Pi 3.14} ;;""")
    assert namespace['HELLO']['theKv']['value']['Pi']['value'] == 3.14

def test_parser_6():
    namespace = parser("""[/HELLO> Lambda <- (1 2 +) ;;""")
    assert namespace['HELLO']['Lambda']['value'][2]['value'] == '+'

def test_parser_7():
    namespace = parser("""[/HELLO> LambdaRef <- `(1 2 +) ;;""")
    assert namespace['HELLO']['LambdaRef']['value'][0]['value'] == 1

def test_parser_7():
    namespace = parser("""[/HELLO> theCurry <- (Answer . 42) ;;""")
    assert len(namespace['HELLO']['theCurry']['value']) == 2
    assert namespace['HELLO']['theCurry']['value'][0] == "Answer"
    assert namespace['HELLO']['theCurry']['value'][1]['value'] == 42

def test_parser_8():
    namespace = parser("""[/HELLO> pre <- (:+ 1 2 3 ;) ;;""")
    assert namespace['HELLO']['pre']['value'][0]['value']['value'] == "+"

def test_parser_8_1():
    namespace = parser("""[/HELLO> pre <- (: (==> 10 +) 1 2 3 ;) ;;""")

def test_parser_8_2():
    namespace = parser("""[/HELLO> pre <- (: (+ . 10) 1 2 3 ;) ;;""")

def test_parser_9():
    namespace = parser("""[/HELLO> Pi <- 3.14 ;;""")
    assert namespace['HELLO']['Pi']['ns'] == "/HELLO"

def test_parser_10():
    namespace = parser("""Pi <- 3.14""")
    assert namespace['__main__']['Pi']['ns'] == '__main__'
