import time
import uuid
import platform
import copy
from socket import gethostname
from queue import LifoQueue
from bund.vm.config import vmConfigNew
from bund.vm.pipes import vmPipesDefaultInit
from bund.library.ns import *
from bund.library.data import *
from bund.ast.value import parse_value
from bund.ast.parser import parserSetup


def vmLang(namespace, lang="bund", **kw):
    sys_lang = kw.get("lang", None)
    if sys_lang is None:
        sys_lang = nsGet(namespace, "/sys/vm.defaultname", None)
        if sys_lang is None:
            nsSet(namespace, "/sys/vm.defaultname", lang)
            return lang
    else:
        nsSet(namespace, "/sys/vm.defaultname", lang)
    return sys_lang


def vmNew(namespace, vmname="bund", **kw):
    lvmname = vmLang(namespace, vmname)
    if lvmname != vmname:
        nsSet(namespace, "/sys/%s/is.ready" % lvmname, False)
        return namespace
    nsSet(namespace, "/sys/vm.hostname", gethostname())
    nsSet(namespace, "/sys/vm.os.system", platform.system())
    nsSet(namespace, "/sys/vm.os.release", platform.release())
    nsSet(namespace, "/sys/vm.hardware", platform.machine())
    nsSet(namespace, "/sys/vm.python", platform.python_version())
    nsSet(namespace, "/sys/modules", [])
    if "is.parser" not in namespace["sys"]:
        nsSet(namespace, "/sys/is.parser", parserSetup(namespace))
    nsNew(namespace, "/sys/%s" % lvmname)
    nsSet(namespace, "/sys/%s/vm.started" % lvmname, time.time())
    nsSet(namespace, "/sys/%s/vm.updated" % lvmname, time.time())
    nsSet(namespace, "/sys/%s/vm.id" % lvmname, str(uuid.uuid4()))
    nsSet(namespace, "/sys/%s/builtins" % lvmname, {})
    nsSet(namespace, "/sys/%s/stack" % lvmname, LifoQueue())
    nsSet(namespace, "/sys/%s/arguments" % lvmname, [])
    nsSet(namespace, "/sys/%s/is.reverse" % lvmname, True)
    nsSet(namespace, "/sys/%s/is.ready" % lvmname, True)
    kw['lang'] = lvmname
    namespace = vmConfigNew(namespace, **kw)
    namespace = vmPipesDefaultInit(namespace, **kw)
    return namespace


def vmGet(namespace, name=None):
    if name is None:
        name = nsGet(namespace, "/sys/vm.defaultname", None)
    if name is None:
        return None
    return nsGet(namespace, "/sys/%s" % name, None)

def vmSys(namespace, name, default=None, **kw):
    lang = vmLang(namespace, **kw)
    _p = "/sys/{}/{}".format(lang, name)
    return nsGet(namespace, _p, default)

def vmSysSet(namespace, **kw):
    lang = vmLang(namespace, **kw)
    for k in kw:
        _p = "/sys/{}/{}".format(lang, k)
        nsSet(namespace, _p, kw[k])
    return namespace

def vmPush(namespace, obj, **kw):
    lang = vmLang(namespace, **kw)
    local_namespace = vmGet(namespace, lang)
    if kw.get("raw", False) is False:
        local_namespace['stack'].put_nowait(parse_value(obj))
    else:
        local_namespace['stack'].put_nowait(obj)
    return namespace

def vmPull(namespace, **kw):
    lang = vmLang(namespace, **kw)
    local_namespace = vmGet(namespace, lang)
    if local_namespace['stack'].empty() is True:
        return None
    return local_namespace['stack'].get_nowait()

def vmPeek(namespace, **kw):
    data = vmPull(namespace, **kw)
    if data is None:
        return data
    kw['raw'] = True
    vmPush(namespace, data, **kw)
    return data

def vmContinue(namespace, **kw):
    data = vmPeek(namespace, **kw)
    return isContinue(data)

def vmStack(namespace, **kw):
    lang = vmLang(namespace, **kw)
    local_namespace = vmGet(namespace, lang)
    while True:
        if local_namespace['stack'].empty() is True:
            break
        next = vmPeek(namespace, **kw)
        if dataType(next).__class__.__name__ == 'PRELIMENARY_EXECUTE_TYPE':
            break
        if dataValue(next) == "%":
            vmPull(namespace, **kw)
            break
        if 'take_only' in kw and dataIsType(next, kw.get('take_only')) is not True:
            break
        next = vmPull(namespace, **kw)
        local_namespace['arguments'].append(next)
    return namespace

def vmArgumentsClear(namespace, **kw):
    vmSysSet(namespace, arguments=[])

def vmArguments(namespace, **kw):
    return vmSys(namespace, "arguments", [])

def vmUnargument(namespaced, **kw):
    args = vmArguments()
    args.reverse()
    for a in args:
        _kw = copy.copy()
        _kw["raw"] = True
        vmPush(namespace, a, **_kw)
    return namespace
