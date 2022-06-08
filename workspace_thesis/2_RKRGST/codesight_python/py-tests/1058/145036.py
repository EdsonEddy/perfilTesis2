n = int(input())
for i in range(n):
    m = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    print(*l)
