def primo(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
             return False
    return True
a,b=map(int,input().split())
ans=0
for i in range(a,b+1):
    if primo(i)==True:
        ans+=1
print(ans)
