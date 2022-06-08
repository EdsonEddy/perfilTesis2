while True:
    try:
        lista = []
        listaA = []
        e = list(map(str, input().split()))
        lista = e
        for i in range(0, len(lista)):
            if lista[i] != '0':
                listaA.append(int(lista[i]))
            else:
                break
        v = int(sum(listaA))
        print(v)
    except ValueError:
        break
