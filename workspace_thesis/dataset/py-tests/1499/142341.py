def a (n,v):
    c=0
    for i in range (1,n):
        if v[i-1]<v[i]:
            c=i
        else:
            break
    for j in range(c+1,n):
        if v[j]==v[j+1]:
            c=j
        else:
            break
    for k in range(c+1,n-1):
        if v[k]>v[k+1]:
            c=k
        else:
            break
    if c==(n-2):
        return True
    else:
        return False
while True:
    n=int(input())
    v= list(map(int,input().split()))
    if a (n,v)or n==1:
        print("SI")
    else:
        print("NO")