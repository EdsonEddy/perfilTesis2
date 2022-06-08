import math
x=int(input())
for i in range(x):
    n=int(input())
    c=1
    num=0
    p=1
    while(n>0):
        d=n%10
        n=n//10
        if(d>1):
            c=1
            i=2
            while(i*i<=d):
                if(d%i==0):
                    c=0
                i=i+1
            if(c==1):
                num=d*p+num
                p=p*10
    print(num)