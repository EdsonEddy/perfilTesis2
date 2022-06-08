e = int(input())
for r in range(e):
    i = 0
    a, b = map(int, input().split())
    while(a >= 3 and b >= 2):
        a = a - 3
        b = b - 2
        i = i + 1
    t = a + b
    print(i,t)