t=input()
g=""
for i in range(len(t)):
    r=str(bin(ord(t[i])))
    r=r[2:]
    r=r.zfill(8)
    g=g+r
print(g)