n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=(a+b)%b
    print(c)