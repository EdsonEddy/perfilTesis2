while True:
    n = int(input())
    d = bin(n)
    f = d[2:len(d)]
    con = 0
    for x in f:
        con+=1
    print(con)