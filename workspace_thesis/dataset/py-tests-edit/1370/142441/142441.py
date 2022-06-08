import sys
for l in sys.stdin:
    n = int(l)
    a=(bin(n))
    print(len(a)-2)