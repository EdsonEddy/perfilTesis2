
n=int(input())
for i in range(n): 
    z=0
    a,b=map(int,input().split())
    x=' ' 
    x=input().split() 
    v=len(x) 
    for i in range(a,b+1): 
        z=z+int(x[i]) 
    print(z)