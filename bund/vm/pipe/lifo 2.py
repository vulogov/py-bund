from queue import LifoQueue
from bund.library.data import *

class fifo_pipe(object): pass

def init(namespace, name, **kw):
    obj = dataMake(LifoQueue(), typeclass=fifo_pipe, **kw)
    dataUpdate(obj, read=read, write=write, seek=None, tell=None, close=None)
    return obj

def read(namespace, pipeObj, **kw):
    return dataValue(pipeObj).get_nowait()

def write(namespace, pipeObj, _data, **kw):
    return dataValue(pipeObj).put_nowait(_data)
