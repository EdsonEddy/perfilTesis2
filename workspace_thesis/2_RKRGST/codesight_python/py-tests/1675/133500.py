t = int(input())
for e in range(t):
    a,b = map(int, input().split())
    print((a*(a+1)//2)*b)