f = open("out2.txt", "wt")
# f.write("Hello!\n") #працює але прінт краще
# f.write(55) # не працює
print("Hello!", file=f)
print(55, file=f)
f.close()