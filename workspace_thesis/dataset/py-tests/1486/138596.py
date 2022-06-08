def fibonaci(k):
    a = 0
    b = 1
    for i in range(k):
        if i % 2 == 0:
            x = a + b
            a = b
            b = x
    return a

n = int(input())
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    else:
        y = fibonaci(i)
        print(y)
    i = i + 1