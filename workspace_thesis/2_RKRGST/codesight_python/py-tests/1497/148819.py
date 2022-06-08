def convertir(x):
    y=str(x)
    deb=y
    while len(deb)!=8:
           deb="0"+deb
    return deb


cad=str(input())
cadim=""
for e in cad:
    conv=ord(str(e))
    bina=bin(conv)
    d=bina[2:]
    f=str(convertir(d))
    cadim=cadim+f
print(cadim)