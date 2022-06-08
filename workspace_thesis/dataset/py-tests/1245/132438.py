a, b = map(int, input().split())
if a > b:
    a, b = b, a
i = b
while i >= a:
    print(i)
    i = i - 1