#скільки цифр(конкретих в числі
d=1257635125412341243125381683157
d=int(input())
freq=[0]*10
while d>0:
    cur = d %10
    freq[cur] += 1
    d=d//10
print(freq)
for el in freq:
    print(el)
for i in range (len(freq)):
    print(f"{i}: {freq[i]}")
for i,el in enumerate(freq):
    print(f"{i}: {freq[i]}")