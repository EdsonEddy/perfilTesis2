t = int(input())
for c in range(t):
    n = int(input())
    a = -1
    b = 1
    fibo = a + b
    for i in range(50):
        if fibo == n:
            print(i)
            break
        a = b
        b = fibo
        fibo = a + b
