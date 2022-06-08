n=int(input())
i=1
sw=0
while i<=n:
    if sw==0:
        j=1
        f=1
        while j<=i:
            f=f*j
            j=j+1
        k=f*(-1)
        print(k)
        sw=1
    else:
        j=1
        f=1
        while j<=i:
            f=f*j
            j=j+1
        print(f)
        sw=0
    i=i+1
