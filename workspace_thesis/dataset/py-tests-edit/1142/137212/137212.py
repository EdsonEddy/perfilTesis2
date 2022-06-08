b,a,n=map(int,input().split())    
s=0
x=n-2
for j in range(x):
    s=(a**2)+b
    b=a
    a=s
    
print (s)