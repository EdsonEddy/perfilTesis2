n=int(input())
a=1
j2=0
j1=0
while a<=n:
    x=int(input())
    if x==2:
        j2=j2+1
        a=a+1
    else:
        j1=j1+1
        a=a+1
if j2>j1:
    print("Gana el jugador 2!")
else:
    print("Gana el jugador 1!")