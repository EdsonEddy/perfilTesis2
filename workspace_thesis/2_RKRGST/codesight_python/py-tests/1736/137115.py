n = int(input())
for i in range(0, n):
    x = 2**i
    y = (2**x)+1
    if i==n-1:
        print(y)
    else:
        print(y, end=" ")