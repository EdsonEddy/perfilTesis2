n = int(input())
for i in range(n):
    m = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(*a)