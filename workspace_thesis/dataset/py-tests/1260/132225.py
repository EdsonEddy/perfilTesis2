def MCD_Euclides(a, b):
    if b == 0:
        return a;
    else:
        return MCD_Euclides(b, a % b)
cantidad=int(input())
i=1
while i<=cantidad:
    cadena=input()
    lista=cadena.split()
    a=int(lista[0])
    b=int(lista[1])
    print(MCD_Euclides(a,b))
    i+=1