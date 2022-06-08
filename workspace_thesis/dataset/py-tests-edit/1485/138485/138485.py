import sys
for n in sys.stdin:
    n = int(n)
    cont = 0
    for i in range (n):
        t = int(input())
        r = 0
        v = int(t)
        while v > 0:
            res = v % 10
            r = (r*10) + res
            v //= 10
        if r == t:
            cont += 1
    print(cont)