import math,sys
def zumba(x):
    for letra in x:
        k="abcdefghijklmnopqrstuvwxyz"
        l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if letra in k:
            return("si es oracion zumba")
        else:
            return("no es oracion zumba")
for x in sys.stdin:        
    n=x
    print(zumba(n))