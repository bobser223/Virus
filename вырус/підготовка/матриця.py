def perevir(lst):
    for i in range(1,len(lst)):
        if lst[i-1] != lst[i]:
            return False
    else:
        return True
def readmatrix(a):
    with open(a) as f:
        size = f.readline()
        matrix = []
        for i in range(int(size)):
            line = f.readline()
            line = line.split()
            matrix.append(line)
    return matrix
print(readmatrix("matrix"))
def mahkvad(a):
    matrix = readmatrix(a)
    if len(matrix) != len(matrix[0]):
        return False
    sum1 = 0
    sum1lst = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sum1 += int(matrix[i][j])
        sum1lst.append(sum1)
        sum1 = 0
    # if perevir(sum1lst) == False:
    #     return False
    sum2 = 0
    sum2lst = []
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            sum2 += int(matrix[i][j])
        sum2lst.append(sum2)
        sum2 = 0
    # if perevir(sum2lst) == False:
    #     return False
    for i in range(len(sum2lst)):
        if sum2lst[i] != sum1lst[i]:
            return False
    else:
        return True
#     # return sum1lst, sum2lst
# print(mahkvad("matrix"))
if mahkvad("matrix"):
    print("ви правильно вирішили судоку")
else:
    print("Попка")