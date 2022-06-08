while True:
    n=int(input())
    lista=list(map(int,input().split()))
    colores=[]
    for i in lista:
        if i not in colores:
            colores.append(i)
    c=0
    sc=0
    for i in colores:
        numero=lista.count(i)
        if numero%2!=0 and numero >2:
            numero=numero-1
        c=numero//2
        sc=sc+c
    print(sc)