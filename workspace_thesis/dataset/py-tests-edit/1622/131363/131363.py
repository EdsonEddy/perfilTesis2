casos=int(input())
while casos>0:
    c=""
    n=int(input())
    a,b=map(int,input().split())
    print(a,end="")
    c=""
    for i in range(n-1):
        a,b=b,(a+b)
        c=c+"+"+str(a)
    print(c)