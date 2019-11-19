import time
from bund.vm.vm import vmGet, vmPush, vmPull, vmPeek, vmContinue

def vmErrorGenerate(**kw):
    err = kw
    err['stamp'] = time.time()
    err['continue'] = False
    if 'msg' not in kw:
        err['msg'] = 'Unidentified error'
    else:
        err['msg'] = err['msg'] % kw
    return err

def vmError(namespace, **kw):
    err = vmErrorGenerate(**kw)
    kw['raw'] = True
    vmPush(namespace, err, **kw)
    return namespace

def vmErrorClear(namespace, **kw):
    handlers = kw.get('handlers', [])
    if vmContinue(namespace, **kw) is True:
        return namespace
    err = vmPull(namespace, **kw)
    if err is None:
        return namespace
    for h in handlers:
        h(namespace, err)
    return namespace

def vmErrorHandler(namespace, **kw):
    handlers = kw.get('handlers', [])
    if len(handlers) == 0:
        return handlers
    if vmContinue(namespace, **kw) is True:
        return namespace
    err = vmPeek(namespace, **kw)
    for h in handlers:
        h(namespace, err, **kw)
    return namespace
