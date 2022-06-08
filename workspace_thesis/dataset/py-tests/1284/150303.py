import math
def tranformar(numero):
    binario = ""
    if (numero > 0):
        while (numero > 0):
            if (numero % 2 == 0):
                binario = "0" + binario
            else:
                binario = "1" + binario
            numero = int(math.floor(numero / 2))
    else:
        if (numero == 0):
            binario = "0"
        else:
            binario = "No se pudo convertir el numero. Ingrese solo numeros positivos"
    return binario
def llenar(x,y):
    t=len(x)
    c=0
    cad=''
    for i in range(t):
        cad=cad+x[c]+y[c]
        c=c+1
    return cad
while 1>0:
    a,b=map(int,input().split())
    e1=tranformar(a)
    e2=tranformar(b)
    v1=[]
    v2=[]
    c=0
    for i in e1:
        v1.insert(c,i)
        c=c+1
    c=0
    for j in e2:
        v2.insert(c,j)
        c=c+1
    c=0
    mos=''
    for i in range(len(v1)):
        mos=mos+v1[c]+v2[c]
        c=c+1
    print(mos)