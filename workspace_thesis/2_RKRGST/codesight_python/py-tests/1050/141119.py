while True:
    def binario(decimal):
        bi = ''
        while decimal // 2 != 0:
            bi = str(decimal % 2) + bi
            decimal = decimal // 2
        return str(decimal) + bi

    n=int(input())
    k=str(binario(n))
    f=k[::-1]
    print(int(f,2))

