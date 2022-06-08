import math
a=int(input(""))
for j in range(1,a+1,1):
    n=int(input(""))
    i=0
    c=0
    x=n
    while c!=100:
        c=c+1
        s=0
        #print("x",x)
        t=int(math.log10(x))+1
        for i in range(1,t+1,1):
            d=x%10
            x=x//10
            #print(d,end="+")
            if(d!=0):
                s=s+(d**2)
        #print("=",s)
        if(s==1):
            break
        else:
            x=s
    if(s==1):
        print("Feliz")
    else:
        print("Triste")