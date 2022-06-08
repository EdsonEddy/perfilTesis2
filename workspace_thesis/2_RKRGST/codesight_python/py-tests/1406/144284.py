n=int(input()) 
while n>0: 
    c=0 
    u=0 
    k=0 
    x=input().split() 
    y=input().split() 
    for i in range(n): 
        s=0 
        s = int(x[i]) + int(y[i])
        k= s + k
        u = k / n 
    for i in range(n): 
            s=0 
            s=int(x[i])+int(y[i])
            if s<u: 
                c=c+1 
    print(c)
    n=int(input())