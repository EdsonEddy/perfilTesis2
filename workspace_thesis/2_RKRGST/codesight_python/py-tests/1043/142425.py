a = int(input())
for i in range(1, a + 1):
    c = 0
    x, y = map(int, input().split())
    while(x >= 3 and y >= 2):
        x = x - 3
        y = y - 2
        c = c + 1
    b = x + y
    print(c, b)