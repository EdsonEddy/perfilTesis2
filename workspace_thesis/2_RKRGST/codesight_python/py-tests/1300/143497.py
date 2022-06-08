while 1>0:
    e=input()
    a= input().split()
    b=a[::-1]
    d=0
    for c in b:
        if c==b[0]:
            d=d+1
    print(d)