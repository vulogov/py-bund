import sys
import os
import platform
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from bund.grammar.internal import *
from bund.language import bundInit
from bund.library.data import *

def test_internal_1():
    namespace = bundInit()
    l = internalMake(namespace, [], 'LAMBDA_TYPE')
    assert dataType(l) == internalClass(namespace, 'LAMBDA_TYPE').__name__
