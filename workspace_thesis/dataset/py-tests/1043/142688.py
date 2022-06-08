casos=int(input())
for i in range(casos):
    a, b= map(int,input().split())
    piedras=a//3
    palitos=b//2

    if piedras > palitos:
        picotas=palitos
    else:
        picotas=piedras
    restop = a - picotas * 3
    restopa = b - picotas * 2
    sobra = restop + restopa
    print(picotas,sobra)