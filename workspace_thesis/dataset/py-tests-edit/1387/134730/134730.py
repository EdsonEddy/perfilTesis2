while True:
    n=int(input())
    a=n
    c=0
    x=0
    while x!=1:
        s=a//10+a%10
        r=str(a%10)+str(s%10)
        c=c+1
        a=int(r)
        if a==n:
            x=1
    print(c)