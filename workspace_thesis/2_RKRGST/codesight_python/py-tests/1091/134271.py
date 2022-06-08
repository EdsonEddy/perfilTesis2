import sys
for x in sys.stdin:
    a,b=map(int,x.split())
    if(a<=100 and b<=100):
        d=b%a
        c=a%b
        if (d==0):
            print (b,"es divisible por",a)
        elif (c==0):
            print (a,"es divisible por",b)
        else:
            print ("-1")