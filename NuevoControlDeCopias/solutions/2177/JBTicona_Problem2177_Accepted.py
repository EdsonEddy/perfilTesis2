def s(n):
    while n>9:
        n1=str(n)
        c=0
        for i in n1:
           c+=int(i)
        n=c
    return n
for _ in range(int(input())):
    a,b=map(int,input().split())
    a1 =list(str(a))
    a2=len(a1)
    n=list()
    while a2 > 0 and len(a1)>=b:
        n.append(int("".join(list(reversed(a1[a2-b:])))))
        del a1[len(a1)-1]
        a2-=1
    res=list()
    for e in n:
        res.append(str(s(e)))
    res.reverse()
    r = ""
    if len(res)==0:
        r+=""
    else:
        for e1 in res:
            r+= e1
    print(r)
