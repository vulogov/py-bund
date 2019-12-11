import copy
from bund.vm.vm import vmGet
from bund.library.data import dataMake

def internalClass(namespace, class_name):
    mm = vmGet(namespace, "metamodel")
    if mm is None:
        return None
    mm_ns = namespace["sys"]["metamodel"].namespaces
    if class_name in mm_ns['__base__']:
        return mm_ns['__base__'][class_name]
    if class_name in mm_ns[None]:
        return mm_ns[None][class_name]
    return None

def internalMake(namespace, data, typeclass, **kw):
    _kw = copy.copy(kw)
    _kw['typeclass'] = internalClass(namespace, typeclass)
    if _kw['typeclass'] is None:
        return None
    return dataMake(data, **_kw)
