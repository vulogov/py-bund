from bund.vm.vm import *
from bund.vm.config import *
from bund.vm.localns import *
from bund.vm.template import *
from bund.vm.runtime_vars import vmRtGet, vmRtSet
from bund.vm.scripts import *
from bund.library.ns import *
from bund.library.log import *
from bund.library.data import *

def bundInit(**kw):
    namespace = nsCreate(**kw)
    log_level = kw.get('loglevel', 'INFO')
    namespace = logInit(namespace, log_level)
    namespace = vmNew(namespace)
    namespace = vmConfigNew(namespace)
    namespace = vmPipesDefaultInit(namespace)
    return namespace
