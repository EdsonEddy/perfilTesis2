import math
n=int(input())
for i in range (n):
    a,b=map(int,input().split())
    if b>=0 and a**b<=2**62:
        a=a**b
        print(a)