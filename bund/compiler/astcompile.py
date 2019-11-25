from bund.compiler.generate import generate
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from bund.ast.parser import parser
from bund.library.ns import nsSet
from bund.language import bundInit
from copy import deepcopy
import time
import calendar

def ast_preserve(namespace, *keys):
    backup = {}
    for k in keys:
        if k in namespace:
            backup[k] = namespace[k]
            namespace[k] = None
    return backup

def ast_compile(namespace, pri, pub):
    if isinstance(namespace, dict) and '__namespace__' in namespace and namespace['__namespace__'] is True:
        cert = x509.load_pem_x509_certificate(pub, default_backend())
        backup = ast_preserve(namespace, "sys", "pipes")
        c_namespace = deepcopy(namespace)
        namespace.update(backup)
        nsSet(c_namespace, "/config/compiled", True)
        nsSet(c_namespace, "/config/compiled.stamp", time.time())
        nsSet(c_namespace, "/config/certificate.issuer", cert.issuer.rfc4514_string())
        nsSet(c_namespace, "/config/certificate.subject", cert.subject.rfc4514_string())
        nsSet(c_namespace, "/config/notvalid.after", calendar.timegm(cert.not_valid_after.timetuple()))
        return generate(c_namespace, pri, pub)
    return None

def ast_compile_src(source, pri, pub, **kw):
    namespace = kw.get("ns", None)
    if namespace is None:
        namespace = bundInit()
    if isinstance(source, str):
        namespace = parser(source, namespace)
        return ast_compile(namespace, pri, pub)
    return None
