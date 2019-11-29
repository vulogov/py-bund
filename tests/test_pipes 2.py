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
    pipeWrite(namespace, pipe, 41)
    answer = pipeRead(namespace, pipe)
    assert dataValue(answer) == 42

def test_pipe_3():
    namespace = bundInit()
    namespace = vmPipeMake(namespace, "test", type="lifo")
    pipe = vmPipeGet(namespace, "test")
    pipeWrite(namespace, pipe, 41)
    pipeWrite(namespace, pipe, 42)
    answer = pipeRead(namespace, pipe)
    assert dataValue(answer) == 42

def test_pipe_4():
    namespace = bundInit()
    namespace = vmPipeMake(namespace, "test", type="random")
    pipe = vmPipeGet(namespace, "test")
    answer = pipeRead(namespace, pipe)
    assert dataIsType(answer, float) == True

def test_pipe_5():
    namespace = bundInit()
    namespace = vmPipeMake(namespace, "test", type="clock")
    pipe = vmPipeGet(namespace, "test")
    answer = pipeRead(namespace, pipe)
    assert dataIsType(answer, float) == True

def test_pipe_6():
    namespace = bundInit()
    pipe = vmPipeGet(namespace, "clock")
    answer = pipeRead(namespace, pipe)
    assert dataIsType(answer, float) == True

def test_pipe_7():
    namespace = bundInit()
    pipe = vmPipeGet(namespace, "random")
    answer = pipeRead(namespace, pipe)
    assert dataValue(answer) > 0.0
    assert dataValue(answer) < 1.0
