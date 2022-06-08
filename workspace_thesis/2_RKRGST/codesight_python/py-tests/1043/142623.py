n=int(input())
if 0 <= n <= 20:
    while n > 0:
        n-=1
        r,p=map(int,input().split())
        c=0
        if 0 <= r <= 10**6  and  0 <= p <= 10**6:
            if r < 3 and p < 2:
                print(0,r+p)
            elif r > p or r < p or r==p:
               c=r//3
               rc=r%3
               if c*2 <= p:
                    rp=p-c*2
                    print(c,rc+rp)
               else:
                   cp=p//2
                   rp=p%2
                   rc=r-cp*3
                   print(cp,rc+rp)
