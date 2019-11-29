from bund.ast.parser import parser
from bund.vm.vm import *
from bund.vm.config import *
from bund.vm.localns import *
from bund.vm.template import *
from bund.vm.runtime_vars import vmRtGet, vmRtSet
from bund.vm.scripts import *
from bund.vm.builtins import vmBuiltinModulesInit
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
    namespace = vmBuiltinModulesInit(namespace, **kw)
    return namespace

def bundParse(namespace, code=None, **kw):
    is_script = kw.get("script", False)
    orig_code = code
    if isinstance(code, str):
        if is_script is True:
            code = vmScriptGet(namespace, code)
        if code is None and isNSID(namespace, code) is True:
            code = nsGet(namespace, code, None)
    elif code is None:
        scripts_list = vmConfigGet(namespace, "main.scripts.path")
        for _code in scripts_list:
            code = vmScriptGet(namespace, _code)
            if isinstance(code, str) is True:
                break
    else:
        return namespace
    if code is None:
        code = orig_code
    if isinstance(code, str) is False:
        return namespace
    return parser(code, namespace)

def bundEval(namespace, **kw):
    return namespace
