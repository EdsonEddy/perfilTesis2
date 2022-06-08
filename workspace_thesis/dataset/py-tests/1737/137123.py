import sys
for x in sys.stdin:
    N=int(x)

    c=0
    r=0
    if (N!=0):
        while(N>0):
            r=1*(10**c)+r
            c=c+1
            N=N-1
            if(N==0):
                print(r)
            else:
                print (r,end=' ')
    else:
        print ("error")
