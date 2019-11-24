from numpy.random import RandomState, SeedSequence
from numpy.random import MT19937
import time
from bund.library.data import *

class random_pipe(object): pass

def init(namespace, name, **kw):
    obj = dataMake(RandomState(MT19937(SeedSequence(int(time.time())))),
        typeclass=random_pipe, **kw)
    dataUpdate(obj, read=read, write=None, seek=None, tell=None, close=None)
    return obj

def read(namespace, pipeObj, **kw):
    return dataMake(dataValue(pipeObj).random())
