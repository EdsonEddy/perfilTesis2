x=int(input())
if x<15:
    import sys
    for y in sys.stdin:
        a,b=map(int,y.split())
        if a>b:
            print(">")
        elif a<b:
            print("<")
        elif a==b:
            print("=")