import math
n=int(input())
c=0
x=0
for i in range(1,n+1,1):
    n=int(input())
    while n > 0:
        a = n%10
        if a == 2 or a == 3 or a == 5 or a ==7:
            c = c+1
            b = a*10**(c-1)
            x = x+ b
        else:
            a = a
        n = int(n/10)
    print(x)
    x = 0
    c = 0
