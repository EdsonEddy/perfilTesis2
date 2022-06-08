n = int(input())
for i in range(n):
    a,m = map(int,input().split())
    c = a % m
    print(c)