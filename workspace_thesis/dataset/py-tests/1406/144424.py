def llenar(n):
    lista=[]
    c=0
    for i in n:
            lista.insert(c, i)
            c = c + 1
    return lista
while 1>0:
    es=int(input())
    x=input().split()
    y=input().split()
    hb=llenar(x)
    hn=llenar(y)
    c=0
    pro=0
    for i in range(es):
        a=int(hb[c])+int(hn[c])
        pro=pro+a
        c=c+1
    pro=pro/es
    c=0
    c2=0
    for i in range(es):
        a=int(hb[c])+int(hn[c])
        if a<pro:
            c2=c2+1
        c=c+1
    print(c2)
