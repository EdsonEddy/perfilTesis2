while True:
    x = input()
    z = list("".join(x))
    res = ''
    for i in range(len(z)):
        foo = ord(z[i])
        aux = bin(foo)
        spam = list("".join(aux[2:]))
        while len(spam)<8:
            spam.reverse()
            spam.append("0")
            spam.reverse()
        au =''
        for j in range(len(spam)):
            au+=spam[j]
        res += au
    print(res)