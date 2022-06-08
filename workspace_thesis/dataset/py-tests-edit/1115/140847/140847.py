def sumaDeDigitos(x):
    segundo=0
    for j in x:
        segundo += int(j)
    return segundo
n=input()
primero=0
c=0
segundo=sumaDeDigitos(n)
for i in range(len(n)-1):
    primero+=int(n[i])
    if primero%3==0 and (segundo-primero)%3==0:
        c+=1
print(c)