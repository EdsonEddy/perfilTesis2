t=int(input())
for j in range(t):
    import math
    aux=int(input())
    c=int(math.log10(aux)+1)
    p=0
    while c>0:
        c=c-1
        d=int(aux/pow(10,c))
        aux=(aux%pow(10,c))
        if(d==2 or d==3 or d==3 or d==5 or d==7):
            p=p*10+d
    if p!=0:
        print(p)
    else:
        print("-1")
