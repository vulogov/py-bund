import msgpack

def pack(obj, **kwargs):
    kwargs.setdefault('use_bin_type', True)
    return msgpack.packb(obj, **kwargs)

def unpack(buf, **kwargs):
    kwargs.setdefault('raw', False)
    return msgpack.unpackb(buf, **kwargs)
