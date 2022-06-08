while True:
    a,b=map(int, input().split())
    while(b != 0):
        a=a % b
        aux = b
        b = a
        a = aux
    if(a == 1):
        print("PRIMOS AMIGOS")
    else:
        print("PRIMOS ENEMIGOS")