x=int(input())
for i in range(x):
    n=int(input())
    s=''
    while n>0:
        d=n%10
        if d==2 or d==3 or d==5 or d==7:
            d=str(d)
            s=d+s
        n=n//10
    if s=='':
        s=0
    print(s)
