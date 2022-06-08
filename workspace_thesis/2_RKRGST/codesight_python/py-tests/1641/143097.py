from sys import stdin,stdout#lectura e impresion rapida

cad,buff=map(str, stdin.readline().split('\n'))
n,buff=map(str,stdin.readline().split('\n'))
n=int(n)
suma=0
for i in range(n):
    x,buff=map(str,stdin.readline().split('\n'))
    x=int(x)
    suma+=x
suma=suma%len(cad)#SACO MODULO
a=cad[(len(cad)-suma):]#DEVUELVE LONGITU DE CADENA MENOS LA SUMA ,RECORTAR EL ULTMO TROZO DE LA CADENA 
b=cad[:(len(cad)-suma)]#COMO FOR DESDE 0 HASTA LA CAD -SUMA
stdout.write(a+b+'\n')