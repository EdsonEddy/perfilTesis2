q=int(input())
t=1
while t <= q:
    t=t+1
    n=int(input())
    a=1
    b=0
    c=0
    x=(n-1)    
    for i in range(0,x):
        c=b
        b=a
        a=c+b
    print(a)

