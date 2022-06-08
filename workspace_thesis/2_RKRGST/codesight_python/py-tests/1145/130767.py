s=int(input())
for j in range(s):
    n = int(input())
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    if n > 0:
        print(b)