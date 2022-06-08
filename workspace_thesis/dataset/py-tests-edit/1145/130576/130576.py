h=int(input())
while h>0:
    m=int(input())
    c,d=0,1
    for i in range(m):
        c,d=d,c+d
        #print(c)
    print(c)
    h=h-1