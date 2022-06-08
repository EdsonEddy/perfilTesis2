n=int(input())
p=0
m=0
for i in range(1,n+1,1):
    c=int(input())
    if(1<=c and c<=2):
        if(c==1):
            p=p+1
        if(c==2):
            m=m+1
if(p>m):
    print("Gana el jugador 1!")
if(m>p):
    print("Gana el jugador 2!")
