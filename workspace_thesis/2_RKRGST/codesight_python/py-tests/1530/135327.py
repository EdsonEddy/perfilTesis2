import math
x=int(input())
for i in range(x):
    n=int(input())
    e=0
    nu=0
    if n>=1 and n<=1000000000:
        while n>0:
            dig=n-(n//10)*10
            n=n//10
            if dig==2 or dig==3 or dig==5 or dig==7:
                nu=int(nu+dig*math.pow(10,e))
                e=e+1
        print(nu)