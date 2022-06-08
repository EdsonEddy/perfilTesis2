def sim(n):
    while n > 26:
        m = n - 26
        n = m
    return n
while True:
    n,k= input().split()
    n = int(n)
    k = k.lower()
    r = sim(n)
    abc = "abcdefghijklmnopqrstuvwxyz"
    ces = ""
    for x in k:
        if x in abc:
            e = abc.index(x) + r
            if e > 25:
                res = e - len(abc)
                x = 0
                d = abc[x+res]
                ces += d
            else:
                f = abc[e]
                ces += f
        elif x == "_":
            ces += " "
        else:
            ces += x
    print(ces.upper()) 
