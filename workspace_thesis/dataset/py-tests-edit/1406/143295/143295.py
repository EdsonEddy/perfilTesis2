while True:
    x=input()
    if x!="":
        x=int(x)
        v = list(map(int,input().split()))
        a = list(map(int, input().split()))
        prom=(sum(v)+sum(a))/x
        c=0
        for i in range(0,x):
            s=a[i]+v[i]
            if s<prom:
                c+=1
        print(c)
    else:
        break