cs=int(input())
while cs>0:
    nm=int(input())
    p=1
    nm=nm%6
    for i in range(nm+1):
        p=p*2
        if p>=10:
            p=p%10+p//10
    print(p)
    cs-=1