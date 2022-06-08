while True:
    try:
        l=[str(x) for x in input().split()]
        x=l[0]
        l.remove(l[0])
        if len(l)==int(x):
            i=l[::-1]
            print(' '.join(i))
    except ValueError:
        break