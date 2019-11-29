from bund.library.ns import *

def vmRtGet(namespace, name, default=None):
    return nsGet(namespace, "/sys/runtime/{}".format(name), default)

def vmRtSet(namespace, name, value):
    return nsSet(namespace, "/sys/runtime/{}".format(name), value)
