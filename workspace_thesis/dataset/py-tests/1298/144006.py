while True:
    l=input().split()
    del l[0]
    a=l[::-1]
    print(" ".join(a))