while True:
    l=list(map(int,input().split()))
    s=0
    for i in l:
        if i!=0:
            s=s+i
        else:
            break
    print(s)