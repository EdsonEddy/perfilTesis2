k=int(input()) 
for i in range(k): 
    s=0 
    m,a,b=map(int,input().split())
    e=' ' 
    e=input().split() 
    for i in range(a,b+1): 
        s=s+int(e[i])
    print(s)