while True:
    n = int(input())
    con = 0
    num = 0
    num1 = 0
    res = 0
    o = list()
    for x in range(0,n):
        con +=1
        num = 2 ** con
        for d in range(con):
            num1 = 2**d
            res = num+num1
            o.append(str(res))
    o = o[0:n]
    o = " ".join(o)
    print(o)
