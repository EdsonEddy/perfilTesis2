import sys
for n in sys.stdin:
    n  = int(n)
    w = list(map(int,input().split()))
    s = True
    m = []
    while w != []:
        wmin = min(w)
        m.append(int(wmin*len(w)))
        v = w
        w = []
        for i in range(len(v)):
            if v[i]>wmin:
                w.append(v[i])
    print(max(m))