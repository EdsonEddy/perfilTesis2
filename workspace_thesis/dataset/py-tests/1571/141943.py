def a (n,v,c):
    for i in range (1,n-1):
        if v[i]<v[i+1]and v[i]<v[i-1]:
            c=c+1
        elif v[i]>v[i+1]and v[i]>v[i-1]:
            c=c+1
    return(c)
while True:
    n=int(input())
    v= list(map(int,input().split()))
    c=0
    print(a (n,v,c))
