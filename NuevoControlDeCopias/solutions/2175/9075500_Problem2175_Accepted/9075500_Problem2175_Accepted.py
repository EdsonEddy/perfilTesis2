casos = (int(input()))
for i in range(0, casos, 1):
    n= int(input())
    a,b = 0,1
    contador = 0
    if (n == a) or (n == b):
        print(n)
    else:
        while (a != n):
            # print(a, end= ' ')
            a,b = b, a+b
            contador += 1
        print(contador)

