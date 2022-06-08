import math
n = int(input())
c = int(math.log(n, 10)+1)
if c%2==1:
    x = int(c/2)+1
    for i in range(1, x+1):
        y = n%10
        n = int(n/10)
    print(y)
else:
    print("*")