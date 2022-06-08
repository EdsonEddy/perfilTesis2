def potencias(n):
    lista=[1]
    s=0
    for l in range (1,n):
        s=2**l
        lista.append(s)
    return lista

listaPotenciasDeDos=potencias(30)
listaDeNumeros=[]
for i in range(0,len(listaPotenciasDeDos)):
    for n in range(1,len(listaPotenciasDeDos)):
        numero=listaPotenciasDeDos[i]+listaPotenciasDeDos[n]
        if numero not in listaDeNumeros:
            if numero not in listaPotenciasDeDos:
                listaDeNumeros.append(numero)
x=sorted(listaDeNumeros)
while True:
    try:
        k=int(input())
        if 1 <= k and k <=400:
            listarequerida=[]
            for u in range(k):
                listarequerida.append(str(x[u]))
            ultimo=' '.join(listarequerida)
            print(ultimo)
    except ValueError:
        break