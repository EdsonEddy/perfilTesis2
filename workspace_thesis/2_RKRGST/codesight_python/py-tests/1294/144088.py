n=int(input())
for i in range(n):
    s=0
    m,a,b=map(int,input().split())
    x=' '
    x=input().split()

    for i in range(a,b+1):
        s=s+int(x[i])
    print(s)