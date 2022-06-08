a,b=0,0
for i in range(int(input())):
    x=int(input())
    if x==1 :
        a=a+1
    else:
        b=b+1
print(["Gana el jugador 1!","Gana el jugador 2!"][b>a])