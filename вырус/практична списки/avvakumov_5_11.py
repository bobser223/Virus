n=int(input())
m= [int(d) for d in input().split()]


p=m
m=tuple(m)

p[0]=m[n-1]
for i in range (n-1):
    p[i+1] = m[i]
print(*p)