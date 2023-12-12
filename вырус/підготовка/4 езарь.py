n = input()
k = int(input())
# chsl = int(input())
# print(ord("a"))
# print(ord("z"))
p = ""
for num in n:
    if num in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        elp = ord(num) - k
        if elp < 65:
            elp = 90 - (65 - elp) + 1
        p += chr(elp)
    elif num in "abcdefghijklmnopqrstuvwxyz":
        elp = ord(num) - k
        if elp < 97:
            elp = 122 - (97 - elp) + 1
        p += chr(elp)
    elif num in " ,":
        p += num
    elif num in "0123456789":
        elp = ord(num) - k
        if elp < 48:
            elp = 57 - (48 - elp) + 1
        p += chr(elp)
    else:
        elp = ord(num) - k
        if elp < 0:
            elp = 0 - (255 - elp) + 1
        p += chr(elp)
print(p)
# Fu|swrorj| lv wkh pdwkhpdwlfv, vxfk dv qxpehu
# wkhru| dqg wkh dssolfdwlrq ri irupxodv dqg dojrulwkpv,
# wkdw xqghuslq fu|swrjudsk| dqg fu|swdqdo|vlv.
# irupxod Q = de prg S, zkhuh 3456<
# Fu|swrorj| lv wkh pdwkhpdwlfv, vxfk dv qxpehu wkhru| dqg wkh dssolfdwlrq ri irupxodv dqg dojrulwkpv, wkdw xqghuslq fu|swrjudsk| dqg fu|swdqdo|vlv. irupxod Q = de prg S, zkhuh 3456<