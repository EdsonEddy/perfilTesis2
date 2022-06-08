n = int(input())
i = 1
while (i <= n):
    d = int(input())
    d = (bin(d).replace('0b', ''))
    d = int(d)
    p = 0
    a = 0
    while (d > 0):
        dig = d % 10
        d = d // 10
        if (dig == 1):
            p = p + 1
            if (p == 2):
                a = a + 1
                p = 0
        else:
            p = 0
    print (a)
    i = i + 1