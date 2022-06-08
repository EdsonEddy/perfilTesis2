palabras=input()
codigo=""
for i in range(len(palabras)):
    cadena=str(bin(ord(palabras[i])))
    cadena=cadena[2:]
    cadena=cadena.zfill(8)
    codigo=codigo+cadena
print(codigo)