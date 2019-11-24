import sys
import os
import platform
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from bund.language import bundInit
from bund.vm.config import *
from bund.vm.pipes import *
from bund.library.data import *

def test_pipe_1():
    namespace = bundInit()
    namespace = vmPipeMake(namespace, "test")
    pipe = vmPipeGet(namespace, "test")
    assert pipe is not None

def test_pipe_2():
    namespace = bundInit()
    namespace = vmPipeMake(namespace, "test")
    pipe = vmPipeGet(namespace, "test")
    pipeWrite(namespace, pipe, 42)
    answer = pipeRead(namespace, pipe)
    assert dataValue(answer) == 42
