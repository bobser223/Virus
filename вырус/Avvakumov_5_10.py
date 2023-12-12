n = input()
lst1 = [i for i in input().split()]
m = input()
lst2 = [i for i in input().split()]
lst3 = []
for i in range(len(lst1)):
    for j in range(len(lst2)):
        if lst1[i] == lst2[j]:
            break
    else:
        lst3.append(lst1[i])
print(len(lst3))
print(*lst3)


# input1 = input()
# lst1 = input1.split()
#
# input2 = input()
# lst2 = input2.split()
#
# lst3 = [item for item in lst1 if item not in lst2]
# print(lst3)
# print(len(lst3))
# print(*lst3)