while 1>0:
    numEst=int(input())
    lista1 = input().split()
    lista2 = input().split()
    lista3 = []

    reprobados=0
    for i, w in enumerate(lista1):
        lista3.append(int(lista1[i]) + int(lista2[i]))

    #print(lista3)
    promedio=(sum(lista3)/numEst)#promedio los que estan por debajo estan reprobados contarlos
    #print(promedio)
    for i in lista3:
        if i <promedio:
            reprobados+=1
    print(reprobados)