def suma(v):
    res=0
    for i in range (len(v)):
        res+=int(v[i])
    return res

from sys import*
for line in stdin:#leeo linea
    v=line.split()#conviertoe en cadenas 
    print(suma(v))
