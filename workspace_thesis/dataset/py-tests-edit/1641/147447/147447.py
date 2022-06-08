from sys import *
cad=stdin.readline().split("\n")
cad=cad[0]
tam=len(cad)
n=int(stdin.readline())
suma=0
for i in range (n):
    x=int(stdin.readline())
    suma=suma + x

suma=suma%tam

aux1=cad[:tam-suma]
aux2=cad[tam-suma:]
print(aux2+""+aux1)

