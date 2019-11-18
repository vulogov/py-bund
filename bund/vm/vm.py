import time
import uuid
import platform
from socket import gethostname
from queue import LifoQueue
from bund.library.ns import *

def vmNew(namespace, vmname="default"):
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
    nsSet(namespace, "/sys/%s/vm.started" % lvmname, time.time())
    nsSet(namespace, "/sys/%s/vm.id" % lvmname, str(uuid.uuid4()))
    nsSet(namespace, "/sys/%s/builtins" % lvmname, {})
    nsSet(namespace, "/sys/%s/stack" % lvmname, LifoQueue)
    nsSet(namespace, "/sys/%s/is.ready" % lvmname, True)
    return namespace


def vmGet(namespace, name=None):
    if name is None:
        name = nsGet(namespace, "/sys/vm.defaultname", None)
    if name is None:
        return None
    return nsGet(namespace, "/sys/%s" % name, None)
