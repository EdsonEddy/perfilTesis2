def a (n,v,k):
    for i in range (0,k):
        a=v[i]*n
        w.append(a)
        w1=max(w)
        n=n-1   
    return(w1)
while True:
    n=int(input())
    k=n
    w=[]
    v= list(map(int,input().split()))
    v= sorted(v)
    print(a (n,v,k))