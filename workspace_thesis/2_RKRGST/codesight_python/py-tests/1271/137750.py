from math import *
n=int(input())
for i in range(n):
    a=int(input())
    o=a
    s=0
    while (a>0):
        d=a%10
        s=s+factorial(d)
        a=a//10
    if (s==o):
        print("Y")
    else:
        print("N")