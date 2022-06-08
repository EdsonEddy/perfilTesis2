t = input()
while t != "fin":
    n = int(t)
    x = 0
    while n != 0:
        x = x + int(input())
        n = n - 1
    print(x)
    t = input()