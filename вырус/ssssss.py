ktest = int(input())

for i in range(ktest):
    numb = []
    knumb = int(input())
    for j in range(knumb):
        numb.append(input())
    dnumb = {num: numb.count(num) for num in numb}
    m = max(dnumb.values())
    list_max = []
    for k, v in dnumb.items():
        if v == m:
            list_max.append(k)
    print(min(list_max))


