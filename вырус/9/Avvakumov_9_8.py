n = input()
lst = [int(i) for i in input().split()]
lst = [abs(num) for num in lst]
print(len(set(lst)))