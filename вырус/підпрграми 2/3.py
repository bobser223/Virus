def minn(a):
    m = a[0]
    for el in a:
        if el < m:
            m = el
    return m


