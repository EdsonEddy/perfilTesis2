n=int(input())
while n > 1:
    s = 0
    while n > 0:
        d = n % 10
        s = s + d * d
        n = n // 10
    n = s
    if n == 0:
        break
if s == 1:
    print(1)
