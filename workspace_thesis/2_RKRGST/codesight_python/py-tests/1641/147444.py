from sys import *
cad = stdin.readline().split("\n")
cad = cad[0]
l = len(cad)
n = int(stdin.readline())
s = 0
for i in range(n):
    x = int(stdin.readline())
    s = x + s
s = s % l

aux = cad[:l - s]
aux1 = cad[l - s:]
print(aux1+aux)
