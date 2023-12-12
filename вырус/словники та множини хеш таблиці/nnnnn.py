n = " 2 3 4  2 3 4 5 4 5 6 2 3 4 5 6 3 4 5 3 4 "
n1 = n.split()
n_d = {m: n1.count(m) for m in n1 }
print(n_d)