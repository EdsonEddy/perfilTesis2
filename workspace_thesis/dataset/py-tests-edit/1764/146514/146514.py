def numeroFeliz(numero):
    c = 0
    s = 0
    while numero > 1 and c < 999:
        s = 0
        while numero > 0:
            d = numero % 10
            s = s + (d * d)
            numero = numero // 10
        numero = s
        if numero == 0:
            break
        c += 1
    if s == 1:
        return True
    else:
        return False

def numeroAbundante(x):
    su = 0
    for i in range(1,x,1):
        if x % i == 0:
            su += i
    if su > x:
        return True
    else:
        return  False


n = 2
menor = 100000
mayor = 0
sumaFelices = 0
sumaAbundantes = 0
while n > -1:
    n = int(input())
    if n == -1:
        break
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n
    if numeroFeliz(n):
        sumaFelices += n
    if numeroAbundante(n):
        sumaAbundantes += n
print(mayor)
print(menor)
print(sumaAbundantes)
print(sumaFelices)