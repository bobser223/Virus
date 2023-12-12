N=int(input())
lst=[int(el) for el in input().split()]

print(*lst)
for step in range (N, 1, -1):
    for i in range(1,step):
        if lst[i-1]>lst[i]:
            lst[i - 1], lst[i]=lst[i],lst[i - 1]

print (*lst)
for step in range (N -1):
    for i in range(1,N-step):
        if lst[i-1]>lst[i]:
            lst[i - 1], lst[i]=lst[i],lst[i - 1]