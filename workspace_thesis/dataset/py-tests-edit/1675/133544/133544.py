p=int(input())
for i in range(p):
    a,b=map(int, input().split())
    v=b*(a*(a+1)//2)
    print(v)