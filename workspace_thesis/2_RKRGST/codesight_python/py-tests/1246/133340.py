while True:
    pa = input()
    s = input()
    d=0
    for x in s:
        if x in pa:
            d += 1
    print (d)