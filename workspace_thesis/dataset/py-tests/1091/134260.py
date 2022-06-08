import sys
for x in sys.stdin:
    a, b = map(int,x.split())
    if a%b==0:
        print(a, "es divisible por", b)
    elif b%a==0:
        print(b, "es divisible por", a)
    else:
        print("-1")