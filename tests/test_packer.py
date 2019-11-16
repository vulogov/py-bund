import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from bund.compiler.pack import pack, unpack

def test_pack_1():
    d = pack(True)
    assert unpack(d) == True

def test_pack_2():
    d = pack({"Привет":"мир"}, use_bin_type=True)
    print(unpack(d))
    assert unpack(d)["Привет"] == "мир"
