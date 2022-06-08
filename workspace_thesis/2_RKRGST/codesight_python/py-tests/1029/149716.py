def llenar(x):
    c=0
    v=[]
    for i in x:
        v.insert(c,int(i))
        c=c+1
    v.sort()
    return (v)
sw=0
while sw==0:
    e=input().split()
    t=len(e)
    if t!=0:
        v=[]
        v=llenar(e)
        c=len(v)-1
        e1=0
        e2=0
        for i in range(len(v)):
            if c%2==0:
                e1=e1+int(v[c])
                c=c-1
            else:
                e2=e2+int(v[c])
                c=c-1

        if e1>=e2:
                s=e1-e2
        else:
                s=e2-e1
        print(s)
    else:
        sw=1