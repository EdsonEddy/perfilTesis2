import math
x=int(input())
s=0
for i in range(x):
    n=int(input())
    t=n
    s=0
    while(n>0):
        d=n%10
        n=n//10
        s=s+math.factorial(d)
    if(t==s):
        print("Y")
    else:
        print("N")