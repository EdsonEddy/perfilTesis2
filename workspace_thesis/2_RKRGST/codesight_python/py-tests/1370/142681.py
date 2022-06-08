while True:
    n=int(input())
    f=bin(n)
    g=f.split("b")
    p=g[1]
    r=len(p)
    print(r)