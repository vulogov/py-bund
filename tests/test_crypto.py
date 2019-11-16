import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
from bund.compiler.crypto import private_key, sign, verify

def test_crypto_1():
    with open("%s/server.key" % tests_dir, "rb") as key_file:
        key = private_key(key_file.read())
        assert key.key_size == 2048

def test_crypto_2():
    with open("%s/server.key" % tests_dir, "rb") as key_file:
        key = private_key(key_file.read())
        sig = sign(key, "Hello world")
        assert len(sig) == 256

def test_crypto3():
    with open("%s/server.key" % tests_dir, "rb") as key_file:
        key = private_key(key_file.read())
        sig = sign(key, "Hello world")
        with open("%s/server.crt" % tests_dir, "rb") as cert_file:
            assert verify(cert_file.read(), sig, "Hello world") == True

def test_crypto4():
    with open("%s/server.key" % tests_dir, "rb") as key_file:
        key = private_key(key_file.read())
        sig = sign(key, "Hello world")
        with open("%s/server.crt" % tests_dir, "rb") as cert_file:
            assert verify(cert_file.read(), sig, "Goodbye cruel world") == False
