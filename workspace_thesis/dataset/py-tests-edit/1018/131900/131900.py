t=int(input())
if t < 15:
    for i in range (1,t+1):
        a,b=map(int,input().split(" "))
        if a>b:
            print(">")
        else:
            if a<b:
                print("<")
            else:
                print("=")
