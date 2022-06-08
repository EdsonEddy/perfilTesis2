import sys
for n in sys.stdin:
    n = int(n)
    p = 1
    x = 0
    for i in range(1, n+1):
        x = x+p
        p = p*10
        if i==n:
            print(x)
        else:
            print(x, end=" ")
    if x==0:
        print("error")