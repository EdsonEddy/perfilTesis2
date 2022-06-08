import sys
for n in sys.stdin:
    for i in range(int(n)):
        a,b=map(int,input().split())
        if a!=b:
            if a>b:
                print(">")
            else:
                print("<")
        else:
            print("=")