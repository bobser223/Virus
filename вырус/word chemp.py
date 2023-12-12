def pol(a):
    if a == a[::-1]:
        return True
    else:
        return False

def chst(a):
    for i in a:
        if i not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890 ":
            a = a.replace(i, "")
    return(a)
def maxx(a: list):
    ma = len(a[0])
    maword = a[0]
    for word in a:
        if len(word) > ma:
            ma = len(word)
            maword = word
    return maword

string = input()
string = string.lower()
string = chst(string)
string = string.split()
string_pol = []
for word in string:
    if pol(word):
        string_pol.append(word)

if len(string_pol) == 0:
    print(0)
else:
    champ = maxx(string_pol)

    for i in range(len(string)):
        if string[i] == champ:
            print(i + 1)
            break
