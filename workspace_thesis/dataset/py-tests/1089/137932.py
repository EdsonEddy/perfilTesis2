import math

n =  int(input())
d = int(math.log10(n)+1)
if d%2==0:
    print('*')
else:
    d2 = int(d/2+1)
    for i in range(d2):
        m = n%10
        n = int(n/10)
    print(m)