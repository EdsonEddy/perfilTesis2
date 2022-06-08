while True:
    n = input()
    if n == "fin":
        break
    m = int(n)
    p = 0
    for i in range(m):
        x =int(input())
        p = p + x
    print(p)