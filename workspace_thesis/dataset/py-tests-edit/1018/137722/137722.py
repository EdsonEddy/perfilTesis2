n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a==b:
        print("=")
    if a>b:
        print(">")
    if a<b:
        print("<")