n=int(input())
for i in range (n):
    x=int(input())
    a=0
    b=1
    C=0
    for j in range (x):
        c=a+b
        b=a
        a=c
    print(c)    
