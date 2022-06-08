cas=int(input())
while cas>0:
    n=int(input())
    p=1
    n=n%6
    for i in range(n+1):
        p=p*2
        if p>=10:
            p=p%10+p//10
    print(p)
    cas-=1