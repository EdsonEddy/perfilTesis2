n=int(input())
for j in range(n):
    x=int(input())
    r=x%6
    if(r==0):
        print("2")
    elif(r==1):
        print("4")
    elif(r==2):
        print("8")
    elif(r==3):
        print("7")
    elif(r==4):
        print("5")
    elif(r==5):
        print("1")
