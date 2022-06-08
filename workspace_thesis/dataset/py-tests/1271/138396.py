import math
def curioso(n):
    a=n
    s=0
    while (n!=0):
        d=n%10
        n=n//10
        s=(math.factorial(d))+s
    if(s==a):
        print("Y")
    else:
        print("N")
n=int(input(""))
for i in range(1,n+1,1):
    x=int(input(""))
    curioso(x)