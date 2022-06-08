t=int(input())
while t>0:
    R=lambda:map(int,input().split())
    a,b=R()
    if a==b:
        print("=")
    elif a>b:
        print(">")
    else:
        print("<")
    t=t-1