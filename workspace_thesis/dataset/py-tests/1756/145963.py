def secuencia(n):
    a=n%6
    q=2**a
    g=q*2
    s=0
    while g>=10:
            d=g%10
            g=g//10
            s=d+g
            g=s
    return g
m=int(input())
for i in range(1,m+1):
    n=int(input())
    o=secuencia(n)
    print(o)