while 1>0:
    a,b=input().split()
    k=int(a)
    abc="abcdefghijklmnopqrstuvwxyz"
    nc=""
    for i in b:
        letra=i
        if letra in abc:           nc=nc+abc[(abc.index(letra)+k)%(len(abc))].upper()
        else:
            if letra == "_":
                nc=nc+" "
            else:
                nc=nc+letra.upper()
    print(nc)