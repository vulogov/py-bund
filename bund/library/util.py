def list_uniq(*lists):
    res = []
    for l in lists:
        res += l
    return list(set(res))
