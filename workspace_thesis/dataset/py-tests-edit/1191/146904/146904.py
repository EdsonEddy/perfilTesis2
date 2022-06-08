while True:
    x=int(input())
    n=list(tuple(map(int,input().split())))
    cupon=int(input())
    n.sort()
    p=None
    mini=0
    maxi=0
    for i in range(len(n)):
        mini=n[i]
        maxi=cupon-mini
        if maxi in n:
            p=True
            break
        else:
            p=False
    if p==True:
        print(mini,maxi)
    else:
        print("-1")
    maxi=0
    mini=0