def common_elements(a, b):
    return list(dict.fromkeys(x for x in a if x in b))
