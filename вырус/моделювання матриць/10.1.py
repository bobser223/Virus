def readmatrix(file):
    M = []
    with open(file) as f:
        N = int(f.readline())
        for i in range(N):
            row = [int(el) for el in f.readline().split()]
            M.append(row)
    return M

M = readmatrix("input.txt")
# def printmatrix(M):
#     for row in M:
#         print(*row)
# printmatrix(readmatrix("input.txt"))
#
# def printmatrix2(M):
#     for row in M:
#         for el in row:
#             print(f"{el:7.1f}", end = "")
#         print()
# printmatrix2(readmatrix("input.txt"))
pencil = 0
counter = 0
for lst in M:
    for numb in lst:
        if numb < 0 and numb % 2 == 0:
            pencil += numb
            counter += 1
print(pencil)
print(counter)

for i in range(M):
    for j in range(len(M[i])):
        if M[i][j] < 0:
            M[i][j] = -M[i][j]

print(M)