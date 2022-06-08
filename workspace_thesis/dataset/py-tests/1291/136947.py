while True:
    h=0
    m=list(map(int,input().split()))
    for i in range(len(m)):
        if m[i]!=0:
            h=h+m[i]
        else:
            break
    print(h)
