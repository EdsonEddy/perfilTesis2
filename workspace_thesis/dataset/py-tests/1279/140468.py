def codificar(mensaje, rotaciones):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabetomayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longitudalfabeto = len(alfabeto)
    codificado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            codificado += letra
            continue
        valorletra = ord(letra)
        alfabetoausar = alfabeto
        limite = 97  
        if letra.isupper():
            limite = 65
            alfabetoausar = alfabetomayusculas
        posicion = (valorletra - limite + rotaciones) % longitudalfabeto
        codificado += alfabetoausar[posicion]
    return codificado
while True:
	rotaciones,mensaje=map(str,input().split())
	rotaciones=int(str(rotaciones))
	codificado = codificar(mensaje, rotaciones)
	ca=str(codificado)
	print(ca.upper().replace('_',' '))