while True:
    elementos=int(input())
    if elementos!=0:
        numeros=list(input().split(" "))
        resultado=""
        numeros.sort(reverse=True)
        for i in numeros:
            resultado=resultado+i
        print(resultado)