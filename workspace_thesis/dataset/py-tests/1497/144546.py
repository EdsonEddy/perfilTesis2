while True:
    x = input()
    binario = ''
    for i in x:
        aux = ord(i)
        b = bin(aux)
        b = b[2:]
        while len(b) < 8:
            b = "0"+b
        binario += b
    print(binario)
