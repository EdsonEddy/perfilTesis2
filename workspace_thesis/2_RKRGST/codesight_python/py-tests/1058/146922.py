n=int(input())
for i in range(n):
    c=int(input())
    o=input().split()
    o.sort(key=int)
    print(*o)