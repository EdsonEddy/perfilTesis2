n=int(input())
contar1=0
contar2=0
for i in range(n):
    m=int(input())
    if m==2:
        contar1=contar1+1
    elif m==1:
        contar2=contar2+1
if contar1>contar2:
    print("Gana el jugador 2!")
else:
    print("Gana el jugador 1!")