from math import log10
while 1:
    a,b=map(int,input().split())
    c=0
    if int(log10(a)+1)==int(log10(b)+1):
        if a>9 and b>9:
            for j in range(int(log10(a)+1)):
                uda=a%10
                udb=b%10
                a=a//10
                b=b//10
                if uda!=udb:
                    c=c+1
            if c<2:
                print("feliz")
            else:
                print("lentes")
        else:
            print("feliz")