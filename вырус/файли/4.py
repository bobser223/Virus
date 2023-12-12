f = open("input.txt", "rt")

print("Read 1")
for line in f:
    print(line, end="")
f.close()

#f.seek(0) # маркер на 0 позицію

f = open("input.txt", "rt")
print("Read 2")
for line in f:
    print(line, end="")
f.close()