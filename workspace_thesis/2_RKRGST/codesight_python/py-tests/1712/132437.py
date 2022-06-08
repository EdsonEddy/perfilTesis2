while True:
    m = input()
    if m == "fin":
        break
    m = int(m)
    s = 0
    for j in range(m):
        x = int(input())
        s = s + x
    print(s)