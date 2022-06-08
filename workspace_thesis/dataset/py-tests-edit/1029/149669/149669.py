import sys
for w in sys.stdin:
    n = w.split()
    cp1 = 0
    cp2 = 0
    l = []
    for i in range(0, len(n)):
        l.append(int(n[i]))
    x = sorted(l)
    a = x[::-1]
    for i in range(0, len(a)):
        if i % 2 == 0:
            cp2 = cp2 + a[i]
        else:
            cp1 = cp1 + a[i]
    if cp2 < cp1:
        d = cp1 - cp2
    else:
        d = cp2 - cp1
    print(d)