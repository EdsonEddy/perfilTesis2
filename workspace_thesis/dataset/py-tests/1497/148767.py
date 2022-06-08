def binario(g):
    r=bin(g)
    r=r[2:]
    r=r.zfill(8)
    return r
c=str(input())
vacio=""
for i in c:
    g=ord(i)
    vacio=vacio+binario(g)
print(vacio)