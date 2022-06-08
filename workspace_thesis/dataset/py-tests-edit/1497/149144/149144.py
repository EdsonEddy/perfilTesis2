def biney(v):
    bin=""
    while v//2!=0:
        bin=str(v%2)+bin
        v=v//2
    return str(v)+bin
v=input()
k=""
for i in v:
    u=ord(i)
    s=biney(u)


    while len(s)!= 8:
        s="0"+s
    k=k+s

print(k)