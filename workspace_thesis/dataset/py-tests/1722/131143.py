n=int(input())
c1=0
c2=0
for i in range(n):
    g=int(input())
    if g==2:
        c2+=1
    elif g==1:
        c1+=1
if c1!=c2:
    if c1>c2:
        print("Gana el jugador 1!")
    else:
        print("Gana el jugador 2!")

