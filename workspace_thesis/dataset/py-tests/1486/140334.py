def fibonacci(n):
    a=0
    b=1
    if n<=1:
        return b
    else:
        for i in range(1,n):
            c=a+b
            a=b
            b=c
        return c

        
x=int(input())
c=0
n=1
d=2
while(c!=x):
    if c%2==0:
        print(fibonacci(n))
        n=n+1
        c=c+1
    else:
        print(d)
        d=d+2
        c=c+1
