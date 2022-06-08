n=int(input())
for i in range(1,n+1,1):
    a,b=map(int,input().split())
    while b>0:
         a,b=b,a%b
    print(a)