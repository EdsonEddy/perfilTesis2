while True:
    p, t = map(int, input().split())
    c = 0
    i = 0
    a = 0
    sum =0
    while a != t:
        sum = sum + a
        a = ((2**i) * p) + a
        # p = p + a
        c += 1
        i +=1
    print(c)
