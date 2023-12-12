n = input()
i=0
for el in n:
    # if el == "-" or el == "+" or el == "*":

    if el in "AEIOUY":
        i += 1
print(i)