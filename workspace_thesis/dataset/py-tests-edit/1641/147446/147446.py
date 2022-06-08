from sys import *
cad =stdin.readline().split("\n")
cad = cad[0]
n = int(stdin.readline())
tam = len(cad)
s = 0
for i in range(n):
    x=int(stdin.readline())
    s = s + x
s = s % tam
aux1 = cad[:tam-s]
aux2 = cad[tam-s:]
print(aux2+""+aux1)
