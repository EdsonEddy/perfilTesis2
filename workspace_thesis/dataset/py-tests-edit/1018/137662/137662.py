import math
n=int(input())
while n>0:
    a,b = map(int,input().split())

    if a>b:
        print(">")
    elif a<b:
        print("<")
    elif a==b:
        print("=")
    n=n-1