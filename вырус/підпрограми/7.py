def inc(lst: list):
    lst.append(1)
    print(lst)
############ main ##########
p = [1, 2, 3]
inc(p.copy())
print(p)