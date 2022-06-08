t=int(input())
for j in range(t):
    import math
    n,k=map(int,input().split())
    aux=n
    p=0
    c=int(math.log10(n))
    #print(c)
    while p<k:
        p=p+1
        d=int(aux/pow(10,c))
        aux=(aux%pow(10,c))
        aux=aux*10+d
    print(aux)
