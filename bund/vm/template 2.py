from jinja2 import Template
from bund.library.ns import *
from bund.vm.vm import *
from bund.vm.config import *
from bund.library.data import *
from bund.library.log import *

def vmTemplate(namespace, name, **kw):
    templates_path = kw.get("templates_path", None)
    if templates_path is None:
        templates_path = vmConfigGet(namespace, "templates.path", ["/templates"])
    for t in templates_path:
        tpl = nsGet(namespace, "{}/{}".format(t, name))
        if tpl is not None:
            return tpl
    return None

def vmTemplateGenerate(namespace, name, **kw):
    tpl = vmTemplate(namespace, name, **kw)
    if tpl is None:
        return None
    t = Template(tpl)
    ns = {}
    ns_list = nsGet(namespace, "/config/templates.namespace", ["/config", "/sys", "/sys/runtime"])
    for n in ns_list:
        ns.update(nsGet(namespace, n))
    ns.update(kw)
    return t.render(**ns)
