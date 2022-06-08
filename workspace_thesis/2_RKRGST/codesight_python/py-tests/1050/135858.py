num = int(input())
while num!="" \
        "":

    cad = ""


    def binary(x):
        global cad
        if x == 0:
            return cad
        else:
            cad = cad + str(x % 2)
        return binary(int(x / 2))


    num = binary(num)
    c, s = 1, 0
    for i in num:
        s = int(i) * (2 ** (len(num) - c)) + s
        c += 1
    print(s)
    num = int(input())