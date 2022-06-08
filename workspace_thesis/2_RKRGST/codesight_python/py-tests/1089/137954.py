import math
def medio (n):
    n = int(n)
    lon = int(math.log10(n))+1
    res1=0
    c=1
    while (True):
        if(c==(lon//2) + 1):
            res1 = n%10
            break
        n//=10
        c+=1
    return res1

n = int(input())
res=0
lon1 = int(math.log10(n))+1

if (lon1%2 != 0):
    res= medio(n)
    print(res)
else:
    print("*")