n=int(input())
m=2

c=1
for j in range (n):
    x=int(input())
    if (x<=1):
        print ("1")
    else:
        m=2
        x=x-2
        for i in range (x):
            m=m*2
    
        print (m) 