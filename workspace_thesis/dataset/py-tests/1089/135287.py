import math

n = int(input())
d = int(math.log10(n)+1)
if d==1:
    print(n)
elif d%2==0:
    print('*')
else:
    d = int(d/2)
    n = int(n%math.pow(10,d+1))
    m = int(n/math.pow(10,d))
    print(m)