a,b= map(int, input().split())
ans=0
for i in range(a,b+1):
    j=2
    b=1
    while j*j<=i:
        if i%j==0:
            b=0
            break
        j+=1
    if b==1 and i!=1:
        ans=ans+1
print(ans)