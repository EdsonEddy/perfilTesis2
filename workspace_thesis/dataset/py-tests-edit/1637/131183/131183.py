a,b,c= map(int,input().split())
x,y,z= map(int,input().split())
if 0<=a<=5 and 0<=b<=5 and 0<=c<=5 and 0<=x<=5 and 0<=y<=5 and 0<=z<=5:
    if a+x==5:
        if b+y==5:
            if c+z ==5:
                print("Esta es la llave")
            else:
                print("Intenta con otra")
        else:
            print("Intenta con otra")
    else:
        print("Intenta con otra")
