a=input()
b=""
for i in range(len(a)):
    m=str(bin(ord(a[i])))
    m=m[2:]
    m=m.zfill(8)
    b=b+m
print(b)