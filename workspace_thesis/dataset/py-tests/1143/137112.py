c = int(input())
for k in range(c):
    n = int(input())
    a, b, c = -1, 1, 0
    sum = 0
    for i in range(n):
        d = a + b + c
        sum += d
        a = b
        b = c
        c = d
    print(sum)