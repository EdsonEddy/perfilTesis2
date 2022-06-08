x=int(input())
while x!=0:
    x=x-1
    n=int(input())
    s=0
    y=n
    while n>0:
        d=n%10
        n=int(n/10)
        f=1
        for i in range(1,d+1):
            f=f*i
        s=s+f
    if s==y:
        print("Y")
    else:
        print("N")