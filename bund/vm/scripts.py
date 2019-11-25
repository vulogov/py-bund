from bund.library.ns import *
from bund.vm.config import vmConfigGet
from bund.vm.vm import vmGet
from bund.ast.parser import parseIn

def vmScript(namespace, name, script, **kw):
    nsSet(namespace, "/scripts/{}".format(name), script)
    is_Run = vmConfigGet(namespace, "scripts.autorun", False)
    if is_Run is not True:
        is_Run = kw.get('run', False)
    if is_Run is True:
        namespace = parseIn(namespace, script)
    return namespace

def vmScriptGet(namespace, name):
    return nsGet(namespace, "/scripts/{}".format(name), None)
