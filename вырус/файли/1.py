f = open("mufile.rrr", "r+t")
# print(f)
# lines = []
print("Start", file=f)
for el in f:
    # lines.append(el)
    print(el, end="")



f.close()



# print(lines)