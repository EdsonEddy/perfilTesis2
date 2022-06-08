n, k = map(int, input().split())
x = n
cd = 0
while x > 0:
    cd = cd + 1
    x = x // 10
c = 0
while n > 0:
    if cd-k == c:
        d = n % 10
    n = n // 10
    c = c + 1
print(cd, d)
