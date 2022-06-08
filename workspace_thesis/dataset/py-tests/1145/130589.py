h=int(input())
while h > 0:
    m=int(input())
    a,b=0,1
    for i in range (m):
        a,b = b,a+b
        #print (a)
    print (a)
    h=h-1