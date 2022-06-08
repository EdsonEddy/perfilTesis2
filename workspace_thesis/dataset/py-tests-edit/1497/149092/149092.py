h=input()
g=""
for i in range(len(h)):
    c=str(bin(ord(h[i])))
    c=c[2:]
    c=c.zfill(8)#numerodebits
    g=g+c
print(g)



