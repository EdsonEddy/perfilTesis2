n=int(input())
for i in range(n):
    s=0
    a,b=map(int,input().split())
    c=input().split()
    for j in range(a,b+1):
        s+=int(c[j])
    print(s)