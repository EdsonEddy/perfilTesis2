import math
n=int(input())
t=int(math.log10(n)+1)
if t%2==0:
    print("*")
else:
    t=int((t/2))
    for i in range(t):
        n=n/10
    d=int(n%10)
    print(d)