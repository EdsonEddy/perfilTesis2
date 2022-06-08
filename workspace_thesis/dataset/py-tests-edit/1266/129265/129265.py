while 2>0:
    el,v=map(int,input().split())
    x=input().split()
    s=0
    for o in range(el):
        for i in x:
            el=el-1
            e=el
            y=(int(i))
            p = v**e
            r=y*p
            s=s+r
        print(float(s))
        break