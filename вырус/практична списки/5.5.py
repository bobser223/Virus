A = [int(el) for el in input().split()]
B = [int(el) for el in input().split()]
a = [A[2]-A[0], A[3]-A[1]]
b = [B[2]-B[0], B[3]-B[1]]
print (a)
print (b)
len_a = (a[0]**2+a[1]**2)**0.5
len_b = (b[0]**2+b[1]**2)**0.5

dod = [a[0]+b[0], a[1]+b[1]]
print(f"{len_a:0.9f} {len_b:0.9f}")
print(f"{dod:0.9f}")
scal= a[0]*b[0]+a[1]*b[1]
vec=a[0]*b[1]-a[1]*b[0]
print( f"{scal:0.9f}",f"{vec:0.9f}")
vec=abs(vec)
S=vec*0.5
print(f"{S:0.9f}")

