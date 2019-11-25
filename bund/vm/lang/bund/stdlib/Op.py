INTERFACE = {}
OPTIONS={'expand': True}
NAME = "Op"

def actually_plus(namespace):

    return namespace

INTERFACE["+"] = actually_plus
