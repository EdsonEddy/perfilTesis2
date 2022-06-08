n=int(input())
v=list(map(int,input().split()))
flag=0
prev=-1
for i in range (n):
    if (v[i]>prev):
        flag=i
        prev=v[i]
    else:
        break
for i in range(flag+1,n):
    if (v[i]==prev):
        flag=i
        prev=v[i]
    else:
        break
for i in range (flag+1,n):
    if (v[i]<prev):
        flag=i
        prev=v[i]
    else:
        break
if (flag==n-1):
    print("SI")
else:
    print("NO")
