n=int(input())
g=1
j2=0
j1=0
while g<=n:
    k=int(input())
    if k==2:
        j2=j2+1
        g=g+1
    else:
        j1=j1+1
        g=g+1
if j2>j1:
    print("Gana el jugador 2!")
else:
    print("Gana el jugador 1!")
