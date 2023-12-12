fin = open("input10.txt")
content = fin.read()
fin.close()
w1 = "hello"
w2 = "bye"
newcontent = content.replace(w1,w2)


print(newcontent)
fout = open("input10.txt", "w")
print(newcontent, file = fout)
fout.close()