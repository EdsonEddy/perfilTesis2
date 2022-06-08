n=int(input())
for i in range (n):
    x=int(input())
    s=0
    y=x
    while(x>0):
        d=x%10
        x=x//10
        f=1
        for j in range (1,d+1):
            f=f*j
        s=s+f
    if(s==y):
        print("Y")
    else:
        print("N")
