import math
cantidad=int(input())
for j in range (0,cantidad,1):
    n = int(input())

    NN=0
    cnn=0
    if (n>=1 and n<=(10**9)):
        while (n>0):
            d=n%10
            n=int(n/10)

            if (d==2 or d==3 or d==5 or d==7):
                    NN=d*(10**cnn)+NN
                    cnn=cnn+1
    print (NN)              

           
             
