while 1:
    a,b=map(int,input().split())
    s=a
    e=1
    if a!=b:
        while s<=b:
            s=s+a*(2**e)
            e+=1

        r=e-1
        print(r)
    else:
        print(1)