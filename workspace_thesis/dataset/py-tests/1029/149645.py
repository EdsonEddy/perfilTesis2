def uno(x):
    a=0
    v=[]
    for i in x:
        v.insert(a,int(i))
        a=a+1
    v.sort()
    return (v)

sw=0
while sw==0:
    z=input().split()
    t=len(z)
    if (t!=0):
        v=[]
        v=uno(z)
        a=len(v)-1
        m=0
        n=0
        for i in range(len(v)):
            if (a%2==0):
                m=m+int(v[a])
                a=a-1
            else:
                n=n+int(v[a])
                a=a-1
        if (m>=n):
                s=m-n
        else:
                s=n-m
        print(s)
    else:
        sw=1
