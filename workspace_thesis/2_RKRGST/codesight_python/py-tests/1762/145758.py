#mun = ['10','20','20','10','10','30','50','10','20']
while 1>0:
    inu = int(input())
    mun = input().split()
    num = []
    impares = 0
    pares = 0
    for i in mun:
        a = int(i)
        num.append(a)
    #print(num) lista con enteros


    sinRepetidos = list(set(num))
    #print(sinRepetidos)
    respu =[]
    #print(num.count(sinRepetidos[0]))#aqui esta la clave
    tama=len(sinRepetidos)
    while tama >0:
        #print(num.count(sinRepetidos[tama-1]))
        pro = num.count(sinRepetidos[tama - 1])
        respu.append(pro)
        tama-=1
    #print(respu)
    #ahora de respu debemos sacar sus modulos de cada uno y si es diferente de 0 no tiene par si lo tiene aumentar uno a a los impares
    for i in respu:
        a = i//2
        impares= impares + a
    print(impares)