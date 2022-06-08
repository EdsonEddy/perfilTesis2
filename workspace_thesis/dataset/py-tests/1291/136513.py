while True:
    n=input().split()
    b=n.index("0")
    nc=n[:b]
    r=0
    for i in nc:
        r=r+int(i)
    print(r)