def secuencia(p):
    y=p%6
    k=2**y
    h=k*2
    s=0
    while h>=10:
            d=h%10
            h=h//10
            s=d+h
            h=s
    return h
n=int(input())
for i in range(1,n+1):
    k=int(input())
    d=secuencia(k)
    print(d)
        
