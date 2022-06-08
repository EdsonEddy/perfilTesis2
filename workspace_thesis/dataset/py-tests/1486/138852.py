def fibo(c):
    a=1
    b=0
    y=0
    i=1
    if c==0:
        a=1
    else:
        while i<=c:
            i=i+1
            y=b
            b=a
            a=y+b
    return a

n=int(input())
i=1
x=2
c=0
if (n%2==0):
    while i<=(n/2):
        i=i+1
        print(fibo(c))
        print(x)
        x=x+2
        c=c+1
else:
    while i<=(n/2):
        i=i+1
        print(fibo(c))
        print(x)
        x=x+2
        c=c+1
    print(fibo(c))