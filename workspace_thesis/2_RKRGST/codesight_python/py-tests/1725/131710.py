while 1>0:
    precio,total=map(int,input().split())
    contador=0
    contador2 = 0
    if precio==total:
        contador=contador+1
        print(contador)
    else:
        s=0
        while s!=total:
                s=s+((2**contador2)*precio)
                contador2=contador2+1
                contador=contador+1
        print(contador)