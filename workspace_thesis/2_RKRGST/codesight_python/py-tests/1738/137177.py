import sys
for x in sys.stdin:
    
    N=int(x)
    n1=8
    sw=1
    while(N>0):
        if(N==1):
            print (n1)
        else:
            print(n1,end=' ')
        if (sw==1):
            n1=n1+5
           
            sw=2
            
        elif (sw==2):
            n1=n1-4
            sw=3

        elif (sw==3):
            n1=n1-6
            sw=4

        elif (sw==4):
            n1=n1+3
            sw=1

        N=N-1
