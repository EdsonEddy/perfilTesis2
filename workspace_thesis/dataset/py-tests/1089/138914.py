import sys
for n in sys.stdin:
    n=int(n)
    if 1<=n<=9999:
        if n%2==0:
            print("*")
        else:
            y=n%2+n//2
            print(y)