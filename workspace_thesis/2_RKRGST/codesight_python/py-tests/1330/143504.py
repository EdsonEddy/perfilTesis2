r, s=map(str, input().split(" "))
s = int(s)
a = len(r)
b = ""

for i in range(len(r)-s,a,1):
    b = b + r[i]
for j in range(0,len(r)-s,1):
    b = b+r[j]

print(b)
