def nsd(a, b):
    if a < b:
        return nsd(b, a)
    if b == 0:
        return a
    return nsd(b,a % b)
