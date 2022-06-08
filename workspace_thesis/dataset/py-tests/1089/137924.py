import math
n = int(input())
lon = int(math.log10(n))+1
c=1
if (lon%2 != 0):
    while (True):
        if(c==(lon//2) + 1):
            res = n%10
            break
        n//=10
        c+=1
    print(res)
else:
    print("*")

