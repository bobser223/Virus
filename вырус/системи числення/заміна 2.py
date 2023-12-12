n = int(input())
print(bin(n))
n = n >> 1
print(bin(n))
n = n << 1
print(bin(n))
n |= (1 << 0)
print(bin(n))
print(n)
