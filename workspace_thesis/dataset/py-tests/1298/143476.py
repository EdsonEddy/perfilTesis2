while 1>0:
    a=input().split()
    del a[0]
    b=a[::-1]
    c=" ".join(b)
    print(c)