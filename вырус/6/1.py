n = input()
ii = 0
for i in range(1, len(n)):
    if n[i] == "-" or n[i] == "+" or n[i] == "*":
        ii += 1
print(ii)

# for el in n:
#     if el == "-" or el == "+" or el == "*":
#         i += 1
#################################################################
n = input()
i=0
for el in n[1:]:
    # if el == "-" or el == "+" or el == "*":

    if el in "+_*":
        i += 1
print(i)