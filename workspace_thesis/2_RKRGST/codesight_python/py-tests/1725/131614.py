while True:
    k,t = map(int, input().split())
    c=0
    a=2
    po=0
    while po < t:
        d=a*k
        po=d+po
        a=a*2
        c+=1
    print (c)