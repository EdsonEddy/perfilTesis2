n=0
while n!="fin":
    n=str(input())
    if n !="fin":
        n=int(n)
        s=0
        for i in range(1,n+1,1):
            j=int(input())
            s=s+j
        print(s)