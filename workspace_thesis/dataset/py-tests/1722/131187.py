n=int(input())
x=1
j2=0
j1=0
while x<=n:
    y=int(input())
    if y==2:
        j2=j2+1
        x=x+1
    else:
        j1=j1+1
        x=x+1
if j2>j1:
    print("Gana el jugador 2!")
else:
    print("Gana el jugador 1!")