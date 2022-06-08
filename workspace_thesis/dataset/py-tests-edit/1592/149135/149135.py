a = int(input())
lista = []
for i in map(int, input().split()):
    lista.append(i)
c = len(lista)
lis = lista
maxi = 0
sumador = 0
for y in range(a):
    sumador = 0
    for u in lista:
        if(lista[y] == u):
            sumador = sumador + 1
    if(maxi < sumador):
        
        maxi = sumador
h = c - maxi
print(h)

