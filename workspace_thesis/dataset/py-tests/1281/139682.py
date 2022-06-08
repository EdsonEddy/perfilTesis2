import math
while True:
    n = int(input())
    x = int(math.sqrt(n))
    fc = []
    arr =[]
    for i in range(1, x+1):
        if n % i == 0:
            fc.append(i)
    for k in fc:
        arr.append(n//k)
    fc.extend(arr)
    fc = set(fc)
    fc = list(fc)
    fc.sort()
    print('Divisores de '+str(n)+":", end=' ')
    for j in range(len(fc)):
        if n < 10:
            if j == len(fc)-1:
                print(str(fc[j]))
            else:
                print(str(fc[j]), end=' ')
        else:
            if j == len(fc)-1:
                print(fc[j])
            else:
                print(fc[j], end=' ')