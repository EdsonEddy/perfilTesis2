n, m, a, b = map(int, input().split())
if 1 <= n <= 10000 and a < m <= 1000 and b < m <= 1000 and 1 <= a <= 1000 and 1 <= b <= 1000:
    if n == 1:
        print(a % m)
    else:
        while n > 2:
             a, b = b, a + b
             n -= 1
        print(b % m)