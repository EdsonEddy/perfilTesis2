
while 1>0:
    f,x=input().split()
    k=int(f)
    abc="abcdefghijklmnopqrstuvwxyz"
    nc=""
    for i in x:
        letra=i
        if letra in abc:
            nc=nc+abc[(abc.index(letra)+k)%(len(abc))].upper()
        else:
            if letra == "_":
                nc=nc+" "
            else:
                nc=nc+letra.upper()
    print(nc)