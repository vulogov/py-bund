import time
from bund.library.ns import *
from bund.compiler.generate import open_envelope

def ast_read(data, pub):
    namespace = open_envelope(data, pub)
    if not namespace:
        return None
    if not nsGet(namespace, "/config/compiled"):
        return None
    if nsGet(namespace, "/config/notvalid.after") < time.time():
        return None
    return namespace
