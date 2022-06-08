while True:
    nelementos = int(input())
    miArreglo = list(map(int,input().split()))
    miArreglo.sort()
    index = 0
    cin = 0
    posible = nelementos//2
    while index + 1 < len(miArreglo):
        if miArreglo[index] == miArreglo[index+1]:
            index += 2
            cin += 1
        else:
            index += 1
    print(cin)