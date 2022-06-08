d = int(input())
for i in range(d):
    n = int(input())
    x = n
    s = 1
    while n > 1:
        s = 0
        while n > 0:
            d = n % 10
            s = s + d * d
            n = n // 10
        if x == s or s == 145:
            break
        n = s
        if n == 0:
            break
    if s == 1:
        print('Feliz')
    else:
        print('Triste')