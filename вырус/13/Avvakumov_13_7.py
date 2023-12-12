
def a(file):
    f = open(file)
    a = f.readlines()
    f.close()
    a = " ".join(a)
    a = a.split()
    maxx = 0
    w = ""
    for word in a:
        if len(word) > maxx:
            maxx = len(word)
            w = word
    return w

print(a("file_13_7"))

def b(file):
    f = open(file)
    a = f.readlines()
    f.close()
    a = " ".join(a)
    a = a.split()
    return len(a)

print(b("file_13_7"))


def c(file):
    f = open(file)
    a = f.readlines()
    f.close()
    a = " ".join(a)
    a = a.split()
    w = ""
    for word in a:
        if len(word) > 1:
            w = w + word + " "
    return w

print(c("file_13_7"))


def d(file):
    f = open(file)
    a = f.readlines()
    f.close()
    a = " ".join(a)
    a = a.split()
    a = " ".join(a)
    return a

print(d("file_13_7"))

def e(file):
    f = open(file)
    p = []
    while True:
        a = f.readline()
        if len(a) == 0:
            break
        words = a.split()
        if len(a) == 1:
            p.append(a)
        leng = len(a)
        curprop = (80 - len(''.join(words))) // (len(words) - 1)
        ost = (80 - len(''.join(words))) % (len(words) - 1)
        a2 = words[0]
        for i in range(1, len(words)):
            kprop = curprop + (1 if i <= ost else 0)
            a2 += ' ' * kprop + words[i]
        p.append(a2)
    f.close()
    # return p
    f2 = open("H", "wt")
    for el in p:
        print(el, file=f2)
        # print(len(el), file=f2)
    f2.close()
e("file_13_7")