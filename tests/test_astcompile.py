import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from bund.compiler.astcompile import ast_compile_src
from bund.compiler.astread import ast_read


def test_ast_compile1():
    with open("%s/server.key" % tests_dir, "rb") as key_file:
        with open("%s/server.crt" % tests_dir, "rb") as cert_file:
            res = ast_compile_src("[/HELLO> ;;", key_file.read(), cert_file.read())
            assert len(res) > 0

def test_ast_compile2():
    with open("%s/server.key" % tests_dir, "rb") as key_file:
        with open("%s/server.crt" % tests_dir, "rb") as cert_file:
            pri = key_file.read()
            pub = cert_file.read()
            data = ast_compile_src("[/HELLO> ;;", pri, pub)
            assert len(data) > 0
            namespace = ast_read(data, pub)
            assert namespace['HELLO']['__namespace__'] == True
