import sys
import os
import platform
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from bund.library.ring import *

def test_ring_1():
    ring = ringNew()
    assert ringAdd(ring, 0, 1, 2, 3, 4) is True

def test_ring_2():
    ring = ringNew()
    ringAdd(ring, 0, 1, 2, 3, 4)
    assert ringTip(ring) == 0

def test_ring_3():
    ring = ringNew()
    ringAdd(ring, 0, 1, 2, 3, 4)
    assert ringLeft(ring) == 4

def test_ring_4():
    ring = ringNew()
    ringAdd(ring, 0, 1, 2, 3, 4)
    assert ringRight(ring) == 1

def test_ring_5():
    ring = ringNew()
    ringAdd(ring, 0, 1, 2, 3, 4)
    ringTick(ring)
    assert ringTip(ring) == 1

def test_ring_6():
    ring = ringNew()
    ringAdd(ring, 0, 1, 2, 3, 4)
    ringFind(ring, 3)
    assert ringTip(ring) == 3
