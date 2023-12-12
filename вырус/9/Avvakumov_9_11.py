wordscount, stringcount = [int(i) for i in input().split()]
pwords = {}
pwords = set(pwords)
for i in range(wordscount):
    pwords.add(input())
ptext = ""
for i in range(stringcount):
    ptext += input()
    ptext += " "
ptext = ptext.lower()
for el in ptext:
    if el in ":.,;-_'!?" or el in '"':
        ptext = ptext.replace(el, "")

ptext = ptext.split()
ptext = set(ptext)

if pwords.issubset(ptext) and ptext.issubset(pwords):
    print("Everything is going to be OK.")
elif pwords.issubset(ptext):
    print("Some words from the text are unknown.")
else:
    print("The usage of the vocabulary is not perfect.")






