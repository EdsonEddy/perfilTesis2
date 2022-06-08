def secuencia(j):
    o=j%6
    f=2**o
    r=f*2
    s=0
    while r>=10:
            e=r%10
            r=r//10
            s=e+r
            r=s
    return r
n=int(input())
for i in range(1,n+1):
    f=int(input())
    e=secuencia(f)
    print(e)
        