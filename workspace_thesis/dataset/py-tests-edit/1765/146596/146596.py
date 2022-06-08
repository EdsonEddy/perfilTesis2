def zumba(s):
    l=[0,1,1,0,1,0,0,1]
    ty=(s[0])
    xy=ty
    c=0
    q=len(s)
    r=0
    if xy>="A" and xy<="Z":
        ma=0
        mi=1
    else:
        mi=0
        ma=1
    for i in range(len(s)):
        a=s[i]
        if a>="A" and a<="Z":
            aux=ma
        elif a>="a" and a<="z":
            aux=mi
        b=l[i]
        if b==aux:
            c+=1
    if c==q:
        r+=1
    return r


while True:
    s=tuple(input().split())
    r=""
    for a in s:
        r+=str(a)
    w=zumba(r)
    if w==1:
        print("si es oracion zumba")
    else:
        print("no es oracion zumba")