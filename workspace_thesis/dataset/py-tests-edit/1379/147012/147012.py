while True:
    l=int(input())
    if l!=0:
        numero=input().split()
        numero.sort()
        c=""
        for i in range(len(numero)):
            c=numero[i]+c
        print(c)
    else:
        break

