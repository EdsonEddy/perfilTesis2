def GenerarPrimos(x):
    UltimoNumeroPrimo = 2
    i = UltimoNumeroPrimo
    numeros = [True, True] + [True] * (x - 1)
    while UltimoNumeroPrimo ** 2 <= x:
        i += UltimoNumeroPrimo
        while i <= x:
            numeros[i] = False
            i += UltimoNumeroPrimo
        j = UltimoNumeroPrimo + 1
        while j < x:
            if numeros[j]:
                UltimoNumeroPrimo = j
                break
            j += 1
        i = UltimoNumeroPrimo
    return [i + 2 for i, z in enumerate(numeros[2:]) if z]
l=GenerarPrimos(1000005)
t=int(input())
while t >0:
    t-=1
    x=int(input())
    if 4<=x<=1000000:
        for i in range(0,len(l)):
            if i < len(l) - 1:
                if l[i]<=x<=l[i+1]:
                    if x in l:
                        p = l.index(x)
                        print(l[p-1]+l[p+1])
                        break
                    else:
                        print(l[i]+l[i+1])
                        break