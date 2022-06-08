import math
def curioso( t ):
    t = int(t)
    k = t
    res = 0
    while(t>0):
        dig = t % 10
        t//=10
        aux = math.factorial(dig)
        res+=aux
    if (res == k):
        print("Y")
    else:
        print("N")


n = int(input())
for j in range(n):
    x = int(input())
    curioso (x)
        
