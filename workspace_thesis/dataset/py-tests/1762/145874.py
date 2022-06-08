while 1>0:
    n=int(input())
    x=input().split()
    pares=0
    lista=[]
    c=0
    for i in x:
        el=int(i)
        lista.insert(c,i)
        c=c+1
    lista.sort()
    c2=0
    sw=0
    while c2<n:
        elemento = lista[c2]
        co = lista.count(elemento)
        pares = pares + (co // 2)
        c2 = c2 + co
    print(pares)