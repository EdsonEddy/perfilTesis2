casos=int(input())
while casos>0:
    numero=int(input())
    dig=1
    numero=numero%6
    for i in range(numero+1):
        dig=dig*2
        if dig>=10:
            dig=dig%10+dig//10
    print(dig)
    casos-=1