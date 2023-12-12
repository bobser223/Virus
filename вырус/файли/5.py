f = open("input.txt", "rt")


# content = f.read(10)
# print(content)
line = f.readline()
print(line)
lines = f.readlines()
print(lines)


f.close()