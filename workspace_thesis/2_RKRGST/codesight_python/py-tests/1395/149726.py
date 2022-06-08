import math
while(True):
    n=int(input())
    x=0
    for i in range(1,n+1):
        x=math.log10(i)+x
    x=int(x)+1
    print(x)