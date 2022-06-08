n = int(input())
for i in range(n):
    m = int(input())
    a = 1
    b = 0
    for j in range(m):
        c = a + b
        a = b
        b = c
    print(c)