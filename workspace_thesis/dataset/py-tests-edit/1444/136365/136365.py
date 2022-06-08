a = int(input())
while(a != 0):
    def binarizar(decimal):
        binario = ''
        while decimal // 2 != 0:
            binario = str(decimal % 2) + binario
            decimal = decimal // 2
        return str(decimal) + binario

    numero = int(input())
    
    b = str(binarizar(numero))
    print(b.count("11"))
    a = a - 1

