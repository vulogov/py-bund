import sys
import os
import platform
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from bund.language import bundInit
from bund.vm.vm import *
from bund.vm.builtins import *
from bund.library.data import *
from bund.ast.parser import *

def test_dd_1():
    namespace = bundInit()
    namespace = parser("2 2", namespace)
