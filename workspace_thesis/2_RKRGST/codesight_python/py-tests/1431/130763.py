n, m, a, b = map(int, input().split())
s = 0
if a == n:
    s = a
elif b == n:
    s = b
else:
    for j in range(n - 2):
        s = a + b
        a, b = b, s
print(s % m)