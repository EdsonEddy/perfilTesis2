x=int(input())
for g in range(x):
    
    n=int(input())
    a=0
    b=1
    for i in range(n):
        a,b=b,a+b
    print(a)