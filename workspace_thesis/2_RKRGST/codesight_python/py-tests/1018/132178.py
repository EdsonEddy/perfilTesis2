a=int(input())
if(1<=a and a<15):
    for i in range(1,a+1,1):
        b,c=map(int,input().split())
        if(b>c):
            print(">")
        if(c>b):
            print("<")
        else:
            if(b==c):
                print("=")
