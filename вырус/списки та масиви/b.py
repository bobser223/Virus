N=int(input())
# lst=[]
# for i in range(N):
#     a = int(input())
#     lst.append(a)
# print(lst)
lst=[0]*N
for i in range(N):
    lst[i] = int(input())
# print(*lst)
# print(*lst[::-1])
for i in range(N//2):
    lst[i], lst[-1-i] = lst[-1-i],lst[i]


