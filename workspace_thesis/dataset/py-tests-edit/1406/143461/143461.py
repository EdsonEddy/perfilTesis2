f = ''
while True:
    t = 0
    g = 0
    n = input()
    if (str(n) == str(f)):
        break
    else:
        n = int(n)
        for x in range(n):
            c = input().split()
            break
        for w in range(n):
            d = input().split()
            break
        for y in range(len(c)):
            t = t + ( int(c[y]) + int(d[y]) )
        t = t/n
        for y in range(len(c)):
            e = ( int(c[y]) + int(d[y]) )
            if (t > e):
                g = g + 1
        print(g)