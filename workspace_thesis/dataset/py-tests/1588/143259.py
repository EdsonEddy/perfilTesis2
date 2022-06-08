caso_prueba = int(input())
contador = 0

for i in range(caso_prueba):
    a = int(input())

    if 1 <= a <= 10000:
        contador = 0
        v = list(map(int, input().split()))
        for j in range(a):
            if v[j]%3 == 0:
                contador = contador + (v[j]*2)

        print("La suma es", contador)