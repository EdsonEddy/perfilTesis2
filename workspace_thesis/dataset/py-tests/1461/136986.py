def Multiplicacion(y):
    sum=0
    listasum =list(str(y))
    #print(listasum)
    longitud=len(listasum)
    for i in range(0,longitud):
        sum=sum+int(listasum[i])**2
    return sum
while True:
    try:
        n=int(input())
        while n>0:
            n=n-1
            x=int(input())
            if 1 <= x and x <= 10**14:
                cuadrado=x
                numerosumado=0
                listaGenerados=[x]
                while numerosumado != 1 and x != 1:
                    numerosumado=Multiplicacion(cuadrado)
                    cuadrado=numerosumado
                    if cuadrado in listaGenerados:
                        print('Triste')
                        break
                    else:
                        listaGenerados.append(numerosumado)
                        #print(listaGenerados)
                if numerosumado==1 or x==1:
                    print('Feliz')
    except ValueError:
        break