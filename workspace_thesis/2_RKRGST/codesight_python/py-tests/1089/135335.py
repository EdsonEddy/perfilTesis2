import math
n=int(input())
L=int(math.log(n,10))+1
if L%2==0:
    print("*")
else:
    L=int(L/2)
    n=n//(10**L)
    n=n%10
    print(int(n))
