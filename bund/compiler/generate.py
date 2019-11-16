from bund.compiler.crypto import private_key, sign, verify
from bund.compiler.pack import pack, unpack
import time
import uuid

def generate(obj, pri, cert):
    pkey = private_key(pri)
    data = pack(obj)
    sig = sign(pkey, data)
    envelope = {'stamp':time.time(), '_id': str(uuid.uuid4())}
    envelope['signature'] = sig
    envelope['certificate'] = cert
    envelope['msg'] = data
    return pack(envelope)

def open_envelope(data, cert=None):
    env = unpack(data)
    if cert is not None:
        certificate = cert
    else:
        certificate = env["certificate"]
    if verify(certificate, env["signature"], env["msg"]) is True:
        return unpack(env["msg"])
    return None
