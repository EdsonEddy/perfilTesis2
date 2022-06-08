n=int(input())
for n in range(n):
    u=int(input())
    x=input().split()
    y=[int(i) for i in x]
    y.sort()
    print(*y)