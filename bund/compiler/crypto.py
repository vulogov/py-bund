from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature
from cryptography import x509
from bund.compiler.pack import pack


def private_key(data):
    _private_key = serialization.load_pem_private_key(
        data,
        password=None,
        backend=default_backend()
    )
    return _private_key

def sign(private_key, data):
    if isinstance(data, str):
        _d = data.encode()
    elif isinstance(data, bytes):
        _d = data
    else:
        _d = pack(data)
    sig = private_key.sign(
            _d,
            padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
    return sig

def verify(cert_pem, signature, data):
    if isinstance(data, str):
        _d = data.encode()
    elif isinstance(data, bytes):
        _d = data
    else:
        _d = pack(data)
    cert = x509.load_pem_x509_certificate(cert_pem, default_backend())
    public_key = cert.public_key()
    try:
        public_key.verify(
            signature,
            _d,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
    except InvalidSignature:
        return False
    return True
