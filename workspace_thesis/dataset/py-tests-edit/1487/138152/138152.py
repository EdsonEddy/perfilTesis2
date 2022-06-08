import math
while(True):
    n=int(input())
    sw=True
    if n<2:
       sw=False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            sw=False
            break
    if sw==True:
        print("ES PRIMO")
    else:
        print("NO ES PRIMO")
         