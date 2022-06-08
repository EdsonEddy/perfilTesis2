def llenar(n):
    lista=[]
    c=0
    for i in n:
            lista.insert(c, i)
            c = c + 1
    return lista
tamaño=int(input())
x=input().split()
ar=llenar(x)
c=0
c2=tamaño-1
sw=1
for i in range (tamaño//2):
    if ar[c]!=ar[c2]:
        sw=0
    c=c+1
    c2=c2-1
if sw==1:
    print('SI')
else:
    print('NO')