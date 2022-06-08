def genFib(a, b):
    x = 0
    m = 0
    for i in range(b):
        v.append(1)
    for i in range(a):
        m = i
        for j in range(b):
            x = v[m] + x
            m = m + 1
        v.append(x)
        x = 0


# Principal
n = int(input())
for p in range(n):
    a, b = map(int, input().split())
    v = []
    genFib(a, b)
    for i in range(len(v)):
        if i == a:
            print(v[i])
