import sys
for n in sys.stdin:
    s1 = s2 = 0
    sw = True
    n = int(n)
    while n > 0:
        d = n % 10
        if sw:
            s1 = s1 + d
        else:
            s2 = s2 + d
        n = n // 10
        sw = not sw
    if s1 == s2:
        print("SI")
    else:
        print("NO")