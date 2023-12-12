n=int(input())
import math
m=1
i=0
while i<n:
    i+=1
    m=m*i
n=int(math.log10(m))+1
print (n)