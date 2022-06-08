def inv(de):
    d = str(pa)
    de = ""
    for i in d:
            de = i+de
    de = int(de)
    return de
while True:
    n = int(input())
    con = 0
    for x in range(n):
        pa = int(input())
        res = inv(pa)
        if res == pa:
            con += 1
    print(con)