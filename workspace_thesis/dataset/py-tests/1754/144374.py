import sys

def adyacente(cad,n):
    r="no"
    for i in range (n-1):
        if cad[i]==cad[i+1] and cad[i]!="r" and cad[i]!="l":
            r="si"
    return r

for x in sys.stdin:
    cad = x
    n=len(cad)
    r=adyacente(cad,n)
    print (r)
