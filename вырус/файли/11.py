import os


content = os.listdir(path=".")

print(content)
fname = "input10.txt"
if fname in content:
    f = open(fname)
    print(f.read())
    f.close()
