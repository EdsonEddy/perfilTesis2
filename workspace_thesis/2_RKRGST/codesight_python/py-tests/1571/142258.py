while(True):
    x=int(input())
    v=[]
    v=list(map(int,input().split()))
    c=0
    for i in range(1,x-1):
        if v[i]<v[i-1] and v[i]<v[i+1]:
            c=c+1
        if v[i]>v[i-1] and v[i]>v[i+1]:
            c=c+1
    print(c)   