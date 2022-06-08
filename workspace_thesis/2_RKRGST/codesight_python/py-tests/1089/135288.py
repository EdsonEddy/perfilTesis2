import math
n=int(input(""))
l=int(math.log10(n))+1
if(l==1):
    print(n)
elif(l%2==0):
    print("*")
else:
    l=(l-1)//2
    n=n//(10**l)
    n=n%10
    print(n)