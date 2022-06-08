def par(n):
    for i in range(1,n+1):
        p=i*2
    return p
def fibo(n):
    a=1
    b=0
    for i in range (1,n+1):
        c=a+b
        a=b
        b=c
    return (c)

n=int(input())
c=1
f=1
for i in range (1,n+1):
    if (i%2==0):
        e=par(c)
        c=c+1
        print(e) 
    else:
        g=fibo(f)
        f=f+1
        print(g)
        
    