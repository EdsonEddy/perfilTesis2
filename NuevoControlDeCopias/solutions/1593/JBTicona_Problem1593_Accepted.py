def cinc(n):
    s =0
    while n>=5:
        s+=n//5
        n=n//5
    return s
import sys
for linea in sys.stdin:
    n = int(linea)
    p = []
    for e in range(4,500001):
        if cinc(e)>n:
            break
        elif cinc(e) == n:
            p.append(e)
    if len(p) == 0:
        print(0)
    else:
        print(*p)
