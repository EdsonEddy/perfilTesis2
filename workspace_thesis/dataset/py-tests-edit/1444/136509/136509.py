def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
casos=int(input())
for i in range(casos):
    n=int(input())
    n2=binarizar(n)
    ocurrencias=n2.count("11")
    print(ocurrencias)
        