x=int(input())
for sd in range(x):
    n=int(input())

    n=n%6
    d=2
    s=0
    d = d * 2**n
    if d<10:
        s=d%10
    if d>=10:
        f=str(d)
        s=0
        for h in f:
            s=s+int(h)
        if s>=10:
            p=str(s)
            s=0
            for k in p:
                s=s+int(k)






    print(s)
