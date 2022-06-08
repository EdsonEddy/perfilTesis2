a,b,c = map(int, input().split())
x,y,z = map(int, input().split())

if(a+x==5):
    if(b+y==5):
        if(c+z==5):
            print("Esta es la llave")
        else:
            print ("Intenta con otra")
    else:
        print ("Intenta con otra")
else:
    print ("Intenta con otra")