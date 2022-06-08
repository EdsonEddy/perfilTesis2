import sys
for x in sys.stdin:
    suma=0
    lista=list(map(int,x.split()))
    for i in lista:
        suma=suma+i
    print(suma)