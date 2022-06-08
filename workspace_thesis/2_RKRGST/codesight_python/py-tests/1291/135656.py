import sys
for x in sys.stdin:
    L = list(map(int,x.split()))
    print(sum(L))

