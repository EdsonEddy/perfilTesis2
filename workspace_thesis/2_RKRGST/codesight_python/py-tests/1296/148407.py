casos_prueba = int(input())
ultimaLista = []
for i in range(casos_prueba):
    l = input()
    lista = list(l)
    contLista=0
    for k in lista:
        contLista += 1
    listaUltima = contLista
    newLista = []
    for j in range(listaUltima):
        newLista.append(lista[contLista-1])
        contLista -= 1
    separador = ""
    listaFinal = separador.join(newLista)
    ultimaLista.append(listaFinal)
ultimaLista.reverse()
str1 = ""
for x in ultimaLista:
    str1 = str(x)
    print(str1)