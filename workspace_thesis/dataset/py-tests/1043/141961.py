n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    p=a//3
    p2=b//2
    n1=a%3
    n2=b%2
    if p==p2:
        print(p,n1+n2)
    elif p>p2:
        print(p-(p-p2),n1+n2+(p-p2)*3)
    else:
        print(p2-(p2-p),n1+(p2-p)*2+n2)