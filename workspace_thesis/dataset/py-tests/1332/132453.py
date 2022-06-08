def analizarCaracter(cadena):
    global s
    cadena = cadena.lower()
    for i in range(len(cadena)):
        if cadena[i] not in vocal:
            s = s + '.' + cadena[i]
    return s


# Principal
cad = input()
vocal = ['a', 'e', 'i', 'o', 'u', 'y']
s = ''
t = analizarCaracter(cad)
print(t)