while True:
    v= list(map(int, input().split()))
    for i in range(len(v)-1):
        for j in range(i,-1,-1):
            if v[j+1]>v[j]:
                aux=v[j+1]
                v[j+1]=v[j]
                v[j]=aux
    s,r,sw=0,0,0
    for i in range(len(v)):
        if sw==0:
            s=s+v[i]
            sw=1
        else:
            r=r+v[i]
            sw=0
    if r>s:
        m=r-s
    else:
        m=s-r
    print(m)