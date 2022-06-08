def llenar(x):
    c=0
    b=[]
    for i in x:
        b.insert(c,int(i))
        c=c+1
    b.sort()
    return (b)

sw=0
while sw==0:
    e = input().split()
    t=len(e)
    if t!=0:
        b=[]
        b=llenar(e)
        c=len(b)-1
        e1=0
        e2=0
        for i in range(len(b)):
            if c%2==0:
                e1=e1+int(b[c])
                c=c-1
            else:
                e2=e2+int(b[c])
                c=c-1

        if e1>=e2:
                s=e1-e2
        else:
                s=e2-e1
        print(s)
    else:
        sw=1
