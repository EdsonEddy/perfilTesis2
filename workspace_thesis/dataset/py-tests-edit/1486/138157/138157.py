def fibonacci(n):
    a=1
    b=0
    c=0
    for i in range (1,n+1):
       c=a+b
       a=b
       b=c
    return(c)

m=int(input())
sw=0
a=2
cd=1
for j in range (1,m+1):
    if (sw==0):
        f=fibonacci(cd)
        cd+=1
        print(f)
        sw=1
    else:
        print(a)
        a=a+2
        sw=0
        
        
