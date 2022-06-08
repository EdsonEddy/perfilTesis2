while 2>0:
    from math import log10
    a,b=map(int,input().split())
    d=log10(a)+1
    d1=int(d)
    n1=log10(b)+1
    n2=int(n1)
    c=0
    while a!=0 and b!=0:
        d1=a%10
        a=a//10
        d2=b%10
        b=b//10
        if d1 !=d2:
            c=c+1
        if c==2:
            print("lentes")
            break
    if c !=2:
        print("feliz")