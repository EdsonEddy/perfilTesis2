while 1>0:
    a,b=map(str,input().split())
    a=list(a.split('/'))
    b=list(b.split('/'))
    sw=False
    s=0
    for i in range(len(a)):
        if i >=len(b) :
            l=b
            sw=True
            d=0
            break
        if b[i]=='' and i!=0:
            sw=True
            d=0
            l=a[1:i]
            break
        if a[i]!=b[i]:

            d=i
            break
        else:
            s=s+1
    if sw==False:
        l=a[d:]

    if l=='':
        l=a
    if d!=0:
        u=len(b[d:])
        for i in range(u):
            print('../',end="")
    if sw:
        if len(l)!=1:
            for i in range(s,len(a)):
                if i!=len(a)-1:
                    print(a[i],end="/")
                else:
                    print(a[i])
        else:
            print(l[0])
    else:


        for i in range(len(l)):
            if i!=len(l)-1:
                print(l[i],end="/")
            else:
                print(l[i])
