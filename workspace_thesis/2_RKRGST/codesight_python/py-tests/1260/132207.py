n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    while b>0:
        a,b=b,a%b
    print(a)