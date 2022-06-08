n = int(input())
for x in range(n):
    c = int(input())
    l = list(map(int,input().split()))
    c = len(l)
    B = sorted(l)
    print(*B)
