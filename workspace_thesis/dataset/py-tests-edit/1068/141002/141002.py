def palEnten():#numero de palabras y numero de lineas que entiende
    cont=0
    contadorseguro=-1
    m=int(input())
    while m >0:
        m-=1
        n=input()
        cont+=1
        if n=="porque":
            contadorseguro=cont+contadorseguro
    print(contadorseguro)
x=int(input())
while x >0:
    palEnten()