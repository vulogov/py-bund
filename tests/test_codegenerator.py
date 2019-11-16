import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
from bund.compiler.generate import generate, open_envelope

def test_envelope_1():
    with open("%s/server.key" % tests_dir, "rb") as key_file:
        with open("%s/server.crt" % tests_dir, "rb") as cert_file:
            res = generate({}, key_file.read(), cert_file.read())
            assert len(res) != 0

def test_envelope_2():
    with open("%s/server.key" % tests_dir, "rb") as key_file:
        with open("%s/server.crt" % tests_dir, "rb") as cert_file:
            cert = cert_file.read()
            res = generate({'Hello':'world'}, key_file.read(), cert)
            assert open_envelope(res, cert) != None

def test_envelope_3():
    with open("%s/server.key" % tests_dir, "rb") as key_file:
        with open("%s/server.crt" % tests_dir, "rb") as cert_file:
            cert = cert_file.read()
            res = generate({'Hello':'world'}, key_file.read(), cert)
            d = open_envelope(res)
            assert d != None
            assert d['Hello'] == 'world'
