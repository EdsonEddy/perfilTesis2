def eliminar (x):
    vocales =['a','e','i','o','u','y','A','E','I','O','U','Y']
    resultado = ''
    for letra in x :
        if letra not in vocales:
            resultado=resultado+letra
    return resultado

def insertarpunto (y):
    nuevo=list(y)
    for i in range (0,len(nuevo)*2,2):
           nuevo.insert(i,'.')
    return nuevo
def canbiarMayus(h):
    nuevo=''.join(h)
    nuevo = nuevo.lower()
    return nuevo

nuevo=eliminar(str(input()))
nuevo=insertarpunto(nuevo)
nuevo=canbiarMayus(nuevo)
print(nuevo)