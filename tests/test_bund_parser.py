import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from bund.ast.parser import parser

def test_parser1():
    namespace = parser("""[/HELLO> ;;""")
    assert namespace["HELLO"] == {}
