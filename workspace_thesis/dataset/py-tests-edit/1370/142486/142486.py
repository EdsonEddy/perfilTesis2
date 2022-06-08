import sys
for a in sys.stdin:
    a=int(a)
    b=bin(a)
    c=len(b)-2
    print(c)