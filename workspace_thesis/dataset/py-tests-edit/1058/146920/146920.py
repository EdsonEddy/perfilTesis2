a=int(input())
for i in range(a):
    s=int(input())
    d = input().split()
    d.sort(key=int)
    print(*d)