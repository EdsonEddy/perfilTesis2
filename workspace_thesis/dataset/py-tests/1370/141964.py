import sys
def bin(d):
    c = 1
    while d // 2 != 0:
        c = c + 1
        d = d / 2
    return c

for i in sys.stdin:
    x = int(i)
    print(bin(x))

