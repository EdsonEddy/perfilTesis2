n=int(input())
for i in range(n):
    s=0;
    a,b=map(int,input().split())
 
    x=input().split()
    v=len(x)
    for i in range(a,b+1):
        s=s+int(x[i])
    print(s)