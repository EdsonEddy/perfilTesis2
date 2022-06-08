x=(int(input()))
for i in range(1,x+1,1):
    mcm=0
    a,b=map(int,input().split(" "))
    if(a>b):
        c=a
        a=b
        b=c
    for j in range(1,a+1,1):
        if(a%j==0 and b%j==0):
            mcm=j
    print(mcm)