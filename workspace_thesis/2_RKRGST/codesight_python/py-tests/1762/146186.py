while True:
    a = int(input())
    n = input().split()
    n.sort()
    c = 0
    i = 0
    while (i <= (a - 2)):
        if n[i] == n[i + 1]:
            c += 1
            i += 2
        else:
            i = i + 1

    print(c)