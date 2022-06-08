x=input()
s=""
for i in range(len(x)):
    r=str(bin(ord(x[i])))
    r=r[2:]
    r=r.zfill(8)
    s=s+r
print(s)