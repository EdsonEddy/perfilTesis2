a=input()
z=""
for i in range(len(a)):
    r=str(bin(ord(a[i])))
    r=r[2:]
    r=r.zfill(8)
    z=z+r
print(z)