z = int(input())
for qq in range(z):
    y = 2
    t = 0
    acu = 0
    a = int(input())
    ca = a
    x = 0
    i = 0
    if (int(a) == 0):
        print (y)
    else:
        can = ca // 6
        can = 6 * can
        ca = ca - can 
        tr = y ** (ca+1)
        while (tr > 9):
            while (tr > 0):               
                dig = tr % 10               
                tr = tr // 10               
                acu = acu + dig
            tr = acu
            acu = 0
        print (tr)
