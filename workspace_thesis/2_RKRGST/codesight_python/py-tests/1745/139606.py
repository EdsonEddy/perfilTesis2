c=0
b=0
m=0
while(True):
    
    n=float(input())
    if(n==0):
        break
    if(n>m):
        m=n        
    if(n<0):
        b=b+1
       
    c=c+1
    
p=(100*b)/c
print p
print int(m)