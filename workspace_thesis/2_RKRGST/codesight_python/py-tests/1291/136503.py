while 1>0:
    d=input().split()
    c=0
    for b in d:
        if(b!=" "):
            b=int(b)
            c=c+b
    print(c)