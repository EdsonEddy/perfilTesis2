while True:
    c=int(input())
    l=input().split()
    s=0
    lec=[]
    for i in range(len(l)):
        a=l[i]
        if a not in lec:
            b=l.count(a)
            b=b//2
            s=s+b
        lec.append(a)
    print(s)