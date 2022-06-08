def curioso (t):
    t=int(t)
    s=0
    y=t
    while(t>0):
        d=t%10
        t=t//10
        f=1
        for j in range (1,d+1):
            f=f*j
        s=s+f
    if(s==y):
        print("Y")
    else:
        print("N")
        

n=int(input())
for i in range (n):
    x=int(input())
    curioso(x)
