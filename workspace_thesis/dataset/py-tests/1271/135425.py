cantidad=int(input())
for j in range (cantidad):
    n = int(input())
    f=1
    sf=0
    NN=n
 
    while (n>0):
     d=n%10
     n=int(n/10)
     for i in range (1,d+1,1):
      f=f*i
     sf=sf+f
     f=1
            
    if (NN==sf):
     print("Y")
    else:
     print("N")