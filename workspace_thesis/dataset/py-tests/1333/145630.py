cad = input()
if 1 <= len(cad) <= 100:
    lista = []
    for i in range(len(cad)):
        lista.append(cad[i::])
    lista.sort()
    for i in lista:
        print(i)