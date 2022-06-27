casos = (int(input()))
for i in range(0, casos, 1):
    numero= int(input())
    a,b = 0,1
    contador = 0
    if (numero == a) or (numero == b):
        print(numero)
    else:
        while (a != numero):
            # print(a, end= ' ')
            a,b = b, a+b
            contador += 1
        print(contador)
