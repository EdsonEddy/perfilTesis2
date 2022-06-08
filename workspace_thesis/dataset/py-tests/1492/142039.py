while True:
    t = input()
    c = input()
    pos = 0
    for x in t:
        if x==c:
            print(pos)
        pos += 1
