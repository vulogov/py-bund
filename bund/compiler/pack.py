import msgpack
import zlib

def pack(obj, **kwargs):
    kwargs.setdefault('use_bin_type', True)
    data =  msgpack.packb(obj, **kwargs)
    return zlib.compress(data)

def unpack(buf, **kwargs):
    kwargs.setdefault('raw', False)
    data = zlib.decompress(buf)
    return msgpack.unpackb(data, **kwargs)
