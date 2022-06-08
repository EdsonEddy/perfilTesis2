from sys import *
cad= stdin.readline().split("\n")
cad = cad[0]
n = stdin.readline()
n = int(n)
cant = 0
for i in range(n):
    x = int(stdin.readline())
    cant = cant + x
tam = len(cad)
cant = cant%tam
aux = cad[:tam-cant]
cad = cad[tam-cant:]
print(cad+""+aux)