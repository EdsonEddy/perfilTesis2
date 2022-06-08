while True:
    c=0
    lu=list(map(int,input().split()))
    for i in range(len(lu)):
        if lu[i]!=0:
            c=c+lu[i]
        else:
            break

    print(c)