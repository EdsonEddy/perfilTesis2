for x in range(1,100):
    n=int(input())
    s=0
    if n!="fin":
        for d in range(n):
            m=int(input())
            s=s+m
        print(s)
    else:
        break