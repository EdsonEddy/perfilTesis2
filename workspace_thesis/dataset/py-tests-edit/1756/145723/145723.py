g=int(input())
for g in range(g):
    n=int(input())
    n=n%6
    a=2
    for i in range(n):
        a=int(a)*2
        if len(str(a))!=1:
            s=0
            for k in str(a):
                s=s+int(k)
            a=s
    print(a)