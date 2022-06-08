casos=int(input())
for i in range(casos):
    num=int(input())
    binario=bin(num)
    c=binario.split("b")
    d=c[1]
    s=0
    n=0
    for a in d:
        cc=int(a)
        s=s+cc
        if cc==0:
            s=0
        if s==2:
            n=n+1
            s=0
    print(n)