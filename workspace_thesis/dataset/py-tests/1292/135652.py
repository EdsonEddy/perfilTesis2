while 1>0:
    a=int(input())
    if a==0:
        break
    l=list(map(int,input().split()))

    k=sum(l)
    print(k)