def binario(n):
    sw = False
    cont = 0
    while n > 0:
        r = n % 2
        n = n // 2
        if sw:
            if r == 1:
                cont = cont + 1
            sw = False
        else:
            if r == 1:
                sw = True
    return cont


# Principal
d = int(input())
for i in range(d):
    n = int(input())
    print(binario(n))