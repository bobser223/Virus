def tobin(n):
    b = ""
    while n > 0:
        v = n & 1 # v = n % 2
        b = str(v) + b
        n = n >> 1 # n //= 2
    return b

def todes(b: str):
    b = "110" #n = 6
    pow2 = 1
    for d in b[::-1]:
        n += int(d) * pow2
        pow2 *= 2
    return n

