import math
cont = True
while cont:	
	N = int(input(''))
	if N>=1 and N<=(int(math.pow(10, 18))):
		cont = False

cadena=str(N)
indice=-1
iguales=0
for x in range(0,int(len(cadena)/2)):
    if cadena[x]==cadena[indice]:
        iguales=iguales+1
    indice=indice-1
if iguales==(int(len(cadena)/2)):
    print ('S')
else:
    print ('N')