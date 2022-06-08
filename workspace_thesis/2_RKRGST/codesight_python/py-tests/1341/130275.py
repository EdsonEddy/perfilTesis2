while 2>0:
    n=int(input())
    a=-1
    b=1
    n=n+1
    for i in range(n):
        f=a+b
        a=b
        b=f
    print(f)