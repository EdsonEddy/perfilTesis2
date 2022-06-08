while 1>0:
    a=int(input())
    b=a**(0.5)
    e=int(b)
    d=[]
    h=[]
    j=""
    k=[]
    for c in range(1,e+1):
        if a%c==0:
            d.append(c)
    for f in d:
        g=a//f
        h.append(g)
    d.extend(h)
    d.sort()
    for i in d:
        if i in k:
            continue
        else:
            k.append(i)
    for i in k:
        i=str(i)
        j=j+","+i
    j=j.split(",")
    del(j[0])
    j=" ".join(j)
    l="Divisores de "+str(a)+": "+j
    print(l)
    