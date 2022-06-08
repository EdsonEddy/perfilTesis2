x=int(input())
if x>=1 and x<=99999:
    aux=x
    c=0
    while x>0:
        x=x//10
        c=c+1
    if c/2==c//2:
        print("*")
    else:
        c=(c//2)
        for i in range(1,c+1):
            aux=aux//10
        aux=aux-(aux//10)*10
        print(aux)