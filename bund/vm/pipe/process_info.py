import psutil
from bund.library.data import *

class process_info_pipe(object): pass

def init(namespace, name, **kw):
    obj = dataMake(psutil.Process(),
                   typeclass=process_info_pipe, **kw)
    dataUpdate(obj, read=read, write=None, seek=None, tell=None, close=None)
    return obj

def read(namespace, pipeObj, **kw):
    return dataMake(dataValue(pipeObj).as_dict())
