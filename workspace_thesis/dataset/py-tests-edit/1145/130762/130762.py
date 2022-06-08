n = int(input())
for i in range(n):
    x = int(input())
    a, b = -1, 1
    s = 0
    for j in range(x+1):
        s = a+b
        a, b = b, s
    print(s)