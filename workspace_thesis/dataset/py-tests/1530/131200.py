import math
while True :
    try:
        t=int(input())
        f = 0
        while t > 0:
           t=t-1
           n=int(input())
           nuevo = 0
           if 1<=n and n<=10**9:
               l=int(math.log10(n))+1
               f=0
               while l > 0:
                   l=l-1
                   d=n%10
                   n=n//10
                   if d==2 or d==3 or d==5 or d==7:
                      nuevo=nuevo+d*10**f
                      f=f+1
               print(nuevo)
    except ValueError:
        break