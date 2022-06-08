n=int(input())
for i in range(n):
    cad=input()
    v=list(map(int,cad.split()))
    ans=0
    for i in range(1, len(v)):
        if v[i]>v[i-1]:
            ans+=1
    print(ans)