while True:
    e=[int(x) for x in input().split()]
    v=e[1:]
    print(*reversed(v))