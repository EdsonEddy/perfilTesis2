import math
n=int(input())
for j in range(1,n+1):
    a,b=map(int,input().split())
    if(a>b):
        print(">")
    elif(a<b):
        print("<")
    else:
        print("=")