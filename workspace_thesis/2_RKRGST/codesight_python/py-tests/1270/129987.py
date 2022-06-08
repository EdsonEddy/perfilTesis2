n=int(input())
for i in range(1,n+1,1):
    a=int(input())
    x=a
    s=0
    r=1
    d=0
    if a==0:
        s=1
    if a==1:
        s=0
    while x>1:
        if x%2!=0:
            x=x-1
            d=4
        if x%2==0:
            x=x-2
            s=s+8*r
            r=r*10
    s=s+d*r
    print(s)