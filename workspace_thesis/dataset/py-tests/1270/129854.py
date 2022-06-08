x=int(input())
while x>0:
    y=int(input())
    s=""
    if y>1:
        if (y%2)==1:
            for i in range(1,y,2):
                s=s+str(8)
                i+=i
            print(str(4)+s)

        if (y%2)==0:
            for i in range(1,y,2):
                s=s+str(8)
                i+=i
            print(s)
    if y==1:
        print(0)
    if y==0:
        print(1)