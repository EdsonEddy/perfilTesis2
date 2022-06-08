def obtenerbinarios(v):
    bina=''
    while v//2!=0:
        bina=str(v%2)+bina
        v=v//2
    return str(v)+bina

a=input()
b=''
for j in (a):
    i=ord(j)
    c=obtenerbinarios(i)
    g=len(c)
    while len(c)!=8:
        c='0'+c
    b=b+c
print(b)