def base(n, b):
    n = str(n)
    nn = list("".join(n))
    nn.reverse()
    for i in range(len(nn)):
        nn[i] = int(nn[i])
    s = 0
    c = 0
    for j in range(len(nn)):
        s += nn[j] * b ** c
        c += 1
    return s


while True:
    n, b = map(int, input().split())
    print(base(n, b))