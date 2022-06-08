x=input()
g=""
for i in range(len(x)):
    m=str(bin(ord(x[i])))
    m=m[2:]
    m=m.zfill(8)
    g=g+m
print(g)