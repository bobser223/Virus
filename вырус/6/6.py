# n = input()
# p = ''
# for el in n:
#     if ("0" <= el <= "9" or
#     "a" <= el <= "z" or
#     "A" <= el <= "Z" or el == " "):
#         p += el
# a = n.split()
# print(len(a))
n = input()
p = ''
for el in n:
    if el.isalnum() or el == "":
        p += el
a = n.split()
print(len(a))