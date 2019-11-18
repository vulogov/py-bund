from bund.compiler.generate import generate
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from bund.ast.parser import parser
from bund.library.ns import nsSet
from copy import deepcopy
import time
import calendar

def ast_compile(namespace, pri, pub):
    if isinstance(namespace, dict) and '__namespace__' in namespace and namespace['__namespace__'] is True:
        cert = x509.load_pem_x509_certificate(pub, default_backend())
        c_namespace = deepcopy(namespace)
        c_namespace['sys'] = None
        nsSet(namespace, "/config/compiled", True)
        nsSet(namespace, "/config/compiled.stamp", time.time())
        nsSet(namespace, "/config/certificate.issuer", cert.issuer.rfc4514_string())
        nsSet(namespace, "/config/certificate.subject", cert.subject.rfc4514_string())
        nsSet(namespace, "/config/notvalid.after", calendar.timegm(cert.not_valid_after.timetuple()))
        return generate(namespace, pri, pub)
    return None

def ast_compile_src(source, pri, pub):
    if isinstance(source, str):
        namespace = parser(source)
        return ast_compile(namespace, pri, pub)
    return None
