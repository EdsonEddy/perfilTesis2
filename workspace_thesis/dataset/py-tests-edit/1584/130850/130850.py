while True:
    c=int(input())
    a=input()
    b=0
    d=0
    m=a.split()
    n=0
    for i in m:
        if b==c:
            break
        b=b+1
        i1=int(i)
        if i1 > n:
            n=i1

    min=n
    for i in m:
        if d==c:
            break
        d=d+1
        i2 = int(i)
        if i2 < min:
            min=i2
    dis=n-min
    print(dis)