import time
import uuid
import platform
from socket import gethostname
from queue import LifoQueue
from bund.library.ns import *
from bund.library.data import *
from bund.ast.value import parse_value

def vmNew(namespace, vmname="bund"):
    lvmname = nsGet(namespace, "/sys/vm.defaultname", None)
    if not lvmname:
        lvmname = nsSet(namespace, "/sys/vm.defaultname", vmname)
    else:
        if lvname != vmname:
            nsSet(namespace, "/sys/%s/is.ready" % lvmname, False)
            return namespace
    lvmname = nsSet(namespace, "/sys/vm.defaultname", vmname)
    nsSet(namespace, "/sys/vm.hostname", gethostname())
    nsSet(namespace, "/sys/vm.os.system", platform.system())
    nsSet(namespace, "/sys/vm.os.release", platform.release())
    nsSet(namespace, "/sys/vm.hardware", platform.machine())
    nsSet(namespace, "/sys/vm.python", platform.python_version())
    nsSet(namespace, "/sys/%s" % lvmname, {})
    nsSet(namespace, "/sys/%s/vm.started" % lvmname, time.time())
    nsSet(namespace, "/sys/%s/vm.updated" % lvmname, time.time())
    nsSet(namespace, "/sys/%s/vm.id" % lvmname, str(uuid.uuid4()))
    nsSet(namespace, "/sys/%s/builtins" % lvmname, {})
    nsSet(namespace, "/sys/%s/stack" % lvmname, LifoQueue())
    nsSet(namespace, "/sys/%s/arguments" % lvmname, [])
    nsSet(namespace, "/sys/%s/is.ready" % lvmname, True)
    return namespace


def vmGet(namespace, name=None):
    if name is None:
        name = nsGet(namespace, "/sys/vm.defaultname", None)
    if name is None:
        return None
    return nsGet(namespace, "/sys/%s" % name, None)

def vmPush(namespace, obj, **kw):
    lang = kw.get('lang', 'bund')
    local_namespace = vmGet(namespace, lang)
    if kw.get("raw", False) is False:
        local_namespace['stack'].put_nowait(parse_value(obj))
    else:
        local_namespace['stack'].put_nowait(obj)
    return namespace

def vmPull(namespace, **kw):
    lang = kw.get('lang', 'bund')
    local_namespace = vmGet(namespace, lang)
    if local_namespace['stack'].empty() is True:
        return None
    return local_namespace['stack'].get_nowait()

def vmPeek(namespace, **kw):
    data = vmPull(namespace, **kw)
    if data is None:
        return data
    kw['raw'] = True
    vmPush(namespace, data, **kw)
    return data

def vmContinue(namespace, **kw):
    data = vmPeek(namespace, **kw)
    return isContinue(data)
