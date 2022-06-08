n=int(input())
for i in range(1,n+1,1):
    a=list(input().split())
    a.sort()
    print("Case "+str(i)+":",a[1])
