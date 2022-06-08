a,b=map(int,input().split(" "))
n=int(input())
for i in range(n):
    cad=input()
    v=list(map(int,cad.split()))
    ans=0
    for i in range(len(v)):
        if int(v[i])>=a and int(v[i])<=b: 
            ans+=v[i]
    print(ans)
