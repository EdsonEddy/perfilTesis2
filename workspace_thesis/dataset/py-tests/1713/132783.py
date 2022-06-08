import sys
for l in sys.stdin:
    l =int(l)
    s = 0
    for n in range(l):
        a = int(input())
        s = s + a
    print(s)
    s = 0