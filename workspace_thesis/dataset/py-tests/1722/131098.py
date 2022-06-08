n=int(input())
j1=0
j2=0
for i in range(n):
    k=int(input())
    if k==1:
        j1=j1+1
    if k==2:
        j2=j2+1
if j1>j2:
    print('Gana el jugador 1!')
if j2>j1:
    print('Gana el jugador 2!')
