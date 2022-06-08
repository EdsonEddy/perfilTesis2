n=int(input())

for h in range(0,n,1):
    x=int(input())
    a=1
    b=0
    c=0
    for i in range(0,x,1):
        c=a+b
        #print(c)
        a=b
        b=c
    print(c)