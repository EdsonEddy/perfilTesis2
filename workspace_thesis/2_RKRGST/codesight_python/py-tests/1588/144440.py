casos = int(input())
for i in range(casos):
    num = int(input())
    numbers = input().split()
    su = 0
    for j in numbers:
        aux = int(j)
        if (aux*2)%3==0:
            su += aux * 2
    print('La suma es',su)