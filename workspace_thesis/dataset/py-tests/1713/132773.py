import sys
for linea in sys.stdin:
    n = int(linea)
    s = 0
    for i in  range(n):
        x = int(input())
        s = s + x
    print(s)
