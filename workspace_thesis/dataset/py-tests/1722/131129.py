y = int(input())
c2=0
c=0
for i in range(0, y):
    x = int(input())
    if(x==1):
       c=(c+1)
    else:
        c2=c2+1

if(c>c2):
    print ('Gana el jugador 1!')
else:
    print ('Gana el jugador 2!')