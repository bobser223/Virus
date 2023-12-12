import os

# path = list(os.walk("../../../"))

for path in os.walk("."):
    # print(path[2])
    for file in path[2]:
        print(file)
        # with open(file) as f:
        #     print(f.read())
# print(path)