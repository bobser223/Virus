n = [float(i) for i in input().split()]
m = [float(i) for i in input().split()]

def vzn(n:list, m:list):
   return (n[0] * m[1]) - (n[1] * m[0])

def xvzn(n, m):
    return (n[2] * m[1]) - (n[1] * m[2])
def yvzn(n, m):
    return (n[0] * m[2]) - (n[2] * m[0])

print(xvzn(n,m)/vzn(n,m))
print(yvzn(n,m)/vzn(n,m))

#################################

def readmatrix(file):
    M = []
    with open(file) as f:
        N = int(f.readline())
        for i in range(N):
            row = [int(el) for el in f.readline().split()]
            M.append(row)
    return M
A = readmatrix("input.txt")

d = A[0][0] * A[1][1] - A[0][1] * A[1][0]
dx = A[0][2] * A[1][1] - A[0][1] * A[1][2]
dy = A[0][0] * A[1][2] - A[0][2] * A[1][0]
print(dx/d)
print(dy/d)