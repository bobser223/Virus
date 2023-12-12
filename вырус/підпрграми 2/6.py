#lst = [int(i) for i in input().split()]
###====###
#lst1 = list(map(int, input().split()))
# map - до кожного елементу

def intt(el):
    return int(el)**2
# print(lst)
lst1 = list(map(intt, input().split()))

print(lst1)