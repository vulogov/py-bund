def parse_assignment(namespace, n, a):
    return namespace
def parse_assignments(namespace, n):
    for a in n.statements:
        namespace = parse_assignment(namespace, n, a)
    return namespace
