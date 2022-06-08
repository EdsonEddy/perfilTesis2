from sys import stdin
for n in stdin:
    n = int(n)
    c = 0
    while n > 0:
        x = int(input())
        aux = x
        o = 0
        while x > 0:
            r = (x // 10) * 10
            dig = x - r

            x = x // 10
            o = (o * 10) + dig
        if aux == o:
            c = c + 1
        n = n - 1
    print(c)
