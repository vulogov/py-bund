import time
from bund.vm.vm import vmGet

def vmErrorGenerate(**kw):
    err = kw
    err['stamp'] = time.time()
    err['continue'] = False
    if 'msg' not in kw:
        err['msg'] = 'Unidentified error'
    return err

def vmError(namespace, **kw):
    err = vmErrorGenerate(**kw)
    lang = vmGet()
    lang['queue'].push(err)
    return namespace
