N = 10
f_out= open("out89.txt", "w")
for n in range(1, N):
    print(n**2, file=f_out)
f_out.close()