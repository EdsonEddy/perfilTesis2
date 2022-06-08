while True :
    try:
        n=int(input())
        d=0
        u=0
        while n > 0:
            n=n-1
            c=int(input())
            if c==1:
                    u=u+1
            elif c==2:
                    d=d+1
        if u > d:
            print("Gana el jugador 1!")
        else:
            print("Gana el jugador 2!")
    except ValueError:
        break