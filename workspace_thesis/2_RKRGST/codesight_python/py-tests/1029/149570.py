while True:
    jug = list(map(int,input().split()))
    c,c1, c2 = 0,0,0
    for i in reversed(sorted(jug)):
        c +=1
        if c%2 == 1:
            c1 = c1+i
        else:
            c2 = c2+i
    print(c1-c2)