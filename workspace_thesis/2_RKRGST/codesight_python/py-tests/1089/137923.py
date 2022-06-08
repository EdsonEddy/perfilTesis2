import math
n = int(input())
cd = 1
res=0
lon = int(math.log10(n)) + 1
if(lon % 2!=0):
    while(True):
        if(cd == (lon//2) + 1):
            res = n % 10
            break
        n//=10
        cd+=1
    print(res)
else:
    print("*")