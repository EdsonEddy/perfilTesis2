while True: 
    n=list(map(int,input().split()))
    bolivar=[]
    strongey=[]
    sw=True
    n.sort()
    n.reverse()
    suma=0
    suma2=0
    for q in n:
        if sw:
            bolivar.append(q)
            sw=False
        else:
            strongey.append(q)
            sw=True
    #suma bolivar
    for w in bolivar:
        suma=suma+w
    #suma strongey
    for e in strongey:
        suma2=suma2+e
    
    resultado=suma-suma2
    print(resultado)