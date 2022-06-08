a = input()
c=0
for i in (a) :
    c= c+1
x= 5%2
if (c%2==1 or c==1):
    
    c= int((c+1)/2)
    
    b=0
    for j in (a):
        b=b+1
        if (b==c):
            print (j)
            break
else :
        print ("*")
