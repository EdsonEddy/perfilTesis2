while True:
    n=int(input())
    l=(n//12)//20
    c=(n%12)
    n=(n//12)%20
    r=(l, n, c)
    print(r)
