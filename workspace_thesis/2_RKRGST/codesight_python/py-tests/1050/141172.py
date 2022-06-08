def din(c):
    c =""
    d = bin(n)
    c = d[2:len(d)]
    return c
while True:
    n = int(input())
    fer = din(n)
    de = ""
    for i in fer:
        de = i+de
    inv = int(de,2)
    print(inv)
