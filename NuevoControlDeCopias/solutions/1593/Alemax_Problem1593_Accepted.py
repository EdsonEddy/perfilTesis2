def c(x):
    s =0
    while x>=5:
        s=s+x//5
        x=x//5
    return s
import sys
for linea in sys.stdin:
    x = int(linea)
    f = []
    for i in range(4,500001):
        if c(i)>x:
            break
        elif c(i) == x:
            f.append(i)
    if len(f) == 0:
        print(0)
    else:
        print(*f)
