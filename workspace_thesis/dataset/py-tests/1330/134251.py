a, b = map(str, input().split())
b = int(b)
while(b != 0):
    a = (a[-1] + a[:-1])
    b = b - 1
print(a)
