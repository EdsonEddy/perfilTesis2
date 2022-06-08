import math
t=int(input())
i=0
while i<t:
    a, b=map(int, input().split(" "))
    i=i+1
    if a<b:
             print("<")
    if a>b:
             print(">")
    if a==b:
             print("=")