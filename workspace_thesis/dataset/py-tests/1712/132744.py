while True:
    n =input()
    if n == "fin":
        break
    m = int(n)
    s = 0
    for i in range(m):
        x = int(input())
        s = s + x
    print(s)
