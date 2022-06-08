a, b, n = map(int, input().split())
if n == 1:
    print(a)
elif n == 2:
    print(a + b)
else:
    for i in range(n-2):
        x = (b**2) + a
        a = b
        b = x
print(x)