while 1>0:
    f,a=input().split()
    k=int(f)
    abecedario="abcdefghijklmnopqrstuvwxyz"
    n=""
    for i in a:
        letra=i
        if letra in abecedario:
            n=n+abecedario[(abecedario.index(letra)+k)%(len(abecedario))].upper()
        else:
            if letra == "_":
                n=n+" "
            else:
                n=n+letra.upper()
    print(n)