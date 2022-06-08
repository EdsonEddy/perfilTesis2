while True:
    a,b = map(int,input().split())
    r = max(a+b,a-b,a*b)
    print(r)