t = int(input())
values = [2, 4, 8, 7, 5, 1]
for _ in range(t):
    n = int(input())
    print(values[n%6])