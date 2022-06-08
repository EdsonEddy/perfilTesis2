t=int(input())
for i in range(1,t+1):
    R=lambda:map(int,input().split())
    num1,num2=R()
    if(num1>num2):
        print(">")
    else:
        if(num1<num2):
            print("<")
        else:
            print("=")
