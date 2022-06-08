a=input()
s=""
for i in range(len(a)):
    r=str(bin(ord(a[i])))
    r=r[2:]
    r=r.zfill(8)
    s=s+r
print(s)