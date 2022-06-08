import sys
for n in sys.stdin:
    n = int(n)
    s = 0
    for i in range(n):
        x = int(input())
        s = s + x
    print(s)
