n=int(input())
for i in range(0,n+1):
    a,b=map(int, input().split(" "))
    if a>b:
        print(">")
    elif b>a:
        print("<")
    else:
        print("=")
