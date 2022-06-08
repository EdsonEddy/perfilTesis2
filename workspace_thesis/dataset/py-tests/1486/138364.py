import os
import math
v=lambda:os.system("cls")
def serie (n):
    p=2
    a=1
    b=0
    for i in range(1,n+1,1):

        if(i%2==0):
            print(p)
            p=p+2
        else:
            c=a+b
            print(c)
            a=b
            b=c
n=int(input(""))
serie(n)