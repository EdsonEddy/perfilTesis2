def DecimalaX(n,m):
    if (m > 1 and m < 10):
        lon=(len(str(n)))
        c,p,r=m,0,0
        while lon>0 :
            d1=n%10
            r=r+(d1*(c**p))
            n=n//10
            p=p+1
            lon-=1
        return r
while True:
    try:
        d, b = map(int, input().split())
        print(DecimalaX(d, b))
    except ValueError:
        break
