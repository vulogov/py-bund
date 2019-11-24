import time
from bund.library.data import *

class clock_pipe(object): pass

def init(namespace, name, **kw):
    obj = dataMake(None, typeclass=clock_pipe, **kw)
    dataUpdate(obj, read=read, write=None, seek=None, tell=None, close=None)
    return obj

def read(namespace, pipeObj, **kw):
    return dataMake(time.time())
