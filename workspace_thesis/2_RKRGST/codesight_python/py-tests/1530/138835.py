import math
def cambioPrimos(n):
    lo=int(math.log10(n))
    nn=0
    while n>0:
        d=n//(10**lo)
        if (d==2 or d==3 or d==5 or d==7):
            nn=(nn*10)+d
        n=n%(10**lo)
        lo=lo-1
    return nn
n=int(input())
for i in range (n):
    m=int(input())
    print (cambioPrimos(m))


