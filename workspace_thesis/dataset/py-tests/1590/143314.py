import sys
def sumDig(x):
    s=0
    for i in x:
        s=s+int(i)
    return(s)
    
def suma(v):
    for i in range(1,len(v)):
        v[i]=sumDig(str(i))
while True:
    n,a,b=map(int,input().split())
    sum=0
    v=[0]*(n+1)
    suma(v)
    for i in range(1,n+1):
        if a<=v[i] and v[i]<=b:
            sum=sum+i
    print(sum)  