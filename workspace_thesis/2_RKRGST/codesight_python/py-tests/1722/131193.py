n=int(input())
c=0
p=0
for i in range(1,n+1,1):
    m=int(input())
    if m==1:
        c=c+1
    else:
        p=p+1
if p<c:
    print('Gana el jugador 1!')
else:
    print('Gana el jugador 2!')
