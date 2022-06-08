m=int(input())
while m>0:
    n=int(input())
    a,b=0,1
    for i in range (n):
        a,b=b,a+b
        #print(a)
    print(a)
    m=m-1